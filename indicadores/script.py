from flask import Flask
import pandas as pd
import numpy as np
from google.cloud import storage
from io import StringIO
import os

#editar script para hacer llamado a google storage
app = Flask(__name__)

def get_correlacion_data():
    # Lee el archivo CSV en la misma carpeta
    try:
        credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

        # Usar las credenciales en Google Cloud Storage
        client = storage.Client.from_service_account_json(credentials_path)

        # Especifica el nombre del bucket y el archivo CSV
        bucket_name = "csv_correlacion"
        file_name = 'correlacion.csv'

        # Obtén el bucket
        bucket = client.get_bucket(bucket_name)

        # Obtén el blob (el archivo) dentro del bucket
        blob = bucket.blob(file_name)

        # Descarga el contenido del archivo CSV en memoria
        csv_data = blob.download_as_text()

        # Lee el CSV utilizando pandas desde el texto descargado
        df = pd.read_csv(StringIO(csv_data), sep='\t')

        # Muestra los datos
        print(df.head())  # Muestra las primeras filas del CSV

    except FileNotFoundError:
        print("El archivo 'df.csv' no se encuentra en la carpeta del script.")
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", e)

    # Análisis de correlaciones para todos los pares
    pivoted = df.pivot(index='Date', columns='Symbol', values='ClosePrice')
    correlations = pivoted.corr()
    correlations = correlations.round(2)
    correlations.reset_index(inplace=True)
    correlations.rename(columns={'index': 'Symbol'}, inplace=True)

    # Paso 3: Filtrar correlaciones altas (positivas y negativas)
    threshold = 0.78  # Ajusta este umbral según tus necesidades
    filtered_corr = correlations.loc[:, correlations.columns != 'Symbol']
    high_corr = filtered_corr[(filtered_corr >= threshold) | (filtered_corr <= -threshold)]

# Agregar nuevamente la columna 'Symbol' si la eliminaste
    high_corr = pd.concat([correlations['Symbol'], high_corr], axis=1)
    np.fill_diagonal(high_corr.values, np.nan)  # Ignorar la diagonal principal
    print(high_corr.columns)
    return high_corr, correlations