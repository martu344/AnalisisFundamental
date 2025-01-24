from flask import Flask, jsonify
import pandas as pd
import requests

app = Flask(__name__)


def get_cpi_data(selected_market):
    # economias= ["usd", "EA20"]
    # URL para los datos de inflación (CPI) en EE.UU.
    url = f"https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PRICES@DF_PRICES_ALL,1.0/{selected_market}.M.N.CPI.PA._T.N.GY?startPeriod=2000-05&format=json"

    # configuracion del llamado 
    headers = {
        "Accept": "application/json"
    }

    #llamado
    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error en la solicitud: {response.status_code}")

    #datos
    observations = data['dataSets'][0]['series']['0:0:0:0:0:0:0:0']['observations'] #cpi
    time_periods= data['structure']['dimensions']['observation'] #fecha cpi


    #juntamos los arrays
    dataCPi = {
        'Fecha': [period["name"] for period in time_periods[0]["values"]],  # Extraer las fechas de 'time_periods'
        'CPI': [observations[str(i)][0] for i in range(len(observations))]  # Extraer los valores de CPI de 'observations'
    }

    # Ordenamos el dataframe
    df = pd.DataFrame(dataCPi)
    return df


