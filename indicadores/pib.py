from flask import Flask, jsonify
import pandas as pd
import requests
import json

app = Flask(__name__)


def get_pib_data(selected_market):
    # economias= ["usd", "EA20"]
    # URL para los datos de inflación (CPI) en EE.UU.
    url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA_EXPENDITURE_NATIO_CURR,1.1/Q..USA..........?startPeriod=2023-Q3&dimensionAtObservation=AllDimensions"

    # configuracion del llamado 
    headers = {
        "Accept": "application/json"
    }

    #llamado
    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        data2=json.dumps(data, indent=4)
        print(data)
    else:
        print(f"Error en la solicitud: {response.status_code}")

    #datos
    observations = data['dataSets'][0]['series']['0:0:0:0:0:0:0:0']['observations'] #cpi
    time_periods= data['structure']['dimensions']['observation'] #fecha cpi


    #juntamos los arrays
    dataCPi = {
        'Fecha': [period["name"] for period in time_periods[0]["values"]],  # Extraer las fechas de 'time_periods'
        'Pib': [observations[str(i)][0] for i in range(len(observations))]  # Extraer los valores de CPI de 'observations'
    }

    # Ordenamos el dataframe
    df = pd.DataFrame(dataCPi)
    return df
#df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m') # Convertir la columna 'Fecha' en un formato de fecha que pandas entienda
#df = df.sort_values(by='Fecha') # Ordenar el DataFrame por la columna 'Fecha'
#print(df)


