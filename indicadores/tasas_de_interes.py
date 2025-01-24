from flask import Flask, jsonify
import pandas as pd
import requests

app = Flask(__name__)


def get_tasas_data(selected_market):
#economias = ['AUS','CAN','CHE','NZL','USA','JPN','EA19','GBR','NOR','POL','TUR','DNK','MEX','THA','CHN','ZAF','SWE']

# URL para las tasas de interes en EE.UU.
    url = f"https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_KEI@DF_KEI,4.0/{selected_market}.M.IR3TIB.PA._Z._Z._Z._Z.N?startPeriod=2000-06"

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
    observations = data['dataSets'][0]['series']['0:0:0:0:0:0:0']['observations'] #cpi
    time_periods= data['structure']['dimensions']['observation'] #fecha cpi


    #juntamos los arrays
    data_tasas = {
        'Fecha': [period["name"] for period in time_periods[0]["values"]],  # Extraer las fechas de 'time_periods'
        'Tasa': [observations[str(i)][0] for i in range(len(observations))]  # Extraer los valores de CPI de 'observations'
    }

    # Crear y ordenar DataFrame
    df_tasas = pd.DataFrame(data_tasas)
    return df_tasas
    #df_tasas['Fecha'] = pd.to_datetime(df_tasas['Fecha'], format='%Y-%m')
    #df_tasas = df_tasas.sort_values(by='Fecha')

    # Calcular el cambio porcentual en tasas de interés
    #df_tasas['Diferencial_Porcentual'] = df_tasas['Tasa'].pct_change(periods=1) * 100

    # Asignar puntaje
    #def asignar_puntaje_tasas(cambio_tasa):
    #    if cambio_tasa > 2:
    #        return 5  # Fuerte recomendación de compra
    #    elif 0 < cambio_tasa <= 2:
    #        return 3  # Mantener posición
    #    elif -2 < cambio_tasa <= 0:
    #        return 1  # Posible venta
    #    else:
    #        return 0  # Fuerte venta

    #df_tasas['Puntaje'] = df_tasas['Diferencial_Porcentual'].apply(asignar_puntaje_tasas)

    # Imprimir resultados
    #print(df_tasas[['Fecha', 'Tasa', 'Diferencial_Porcentual', 'Puntaje']])
