from flask import Flask, jsonify
import pandas as pd
import requests
import json

app = Flask(__name__)


def get_sentimiento_data(selected_market):
#economias = ['AUS','CAN','CHE','NZL','USA','JPN','EA19','GBR','NOR','POL','TUR','DNK','MEX','THA','CHN','ZAF','SWE']
    print("llego")
    # URL para las tasas de interes en EE.UU.
    url = f"https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_KEI@DF_KEI,4.0/{selected_market}.M.CCICP.PB...?startPeriod=2000-05&dimensionAtObservation=AllDimensions"

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
    else:
        print(f"Error en la solicitud: {response.status_code}")

    #datos
    observations = data["dataSets"][0]["observations"]
    time_periods = data["structure"]["dimensions"]["observation"][7]["values"]

    # Recorrer las observaciones y enlazar los datos con las fechas
    unemployment_data = []
    for key, values in observations.items():
        time_index = int(key.split(":")[-1])  # Último índice en la clave corresponde al tiempo
        unemployment_rate = values[0]  # El primer valor del array es el dato de desempleo
        
        # Extraer la fecha correspondiente
        date = time_periods[time_index]["id"]
        
        # Guardar la información
        unemployment_data.append((date, unemployment_rate))

    # Ordenamos el dataframe
    df_sentimiento= pd.DataFrame(unemployment_data, columns=["Fecha", "sentimiento"])
    return df_sentimiento
#df_sentimiento['Fecha'] = pd.to_datetime(df_sentimiento['Fecha'], format='%Y-%m') # Convertir la columna 'Fecha' en un formato de fecha que pandas entienda
#df_sentimiento = df_sentimiento.sort_values(by='Fecha') # Ordenar el DataFrame por la columna 'Fecha'
#print(df_sentimiento)





