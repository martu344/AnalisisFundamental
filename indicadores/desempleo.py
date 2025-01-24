from flask import Flask, jsonify
import pandas as pd
import requests

app = Flask(__name__)


def get_desempleo_data(selected_market):
    # URL para las tasas de desempleo
    url = f"https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_KEI@DF_KEI,4.0/{selected_market}.M.UNEMP.PT_LF...?startPeriod=2000-05&dimensionAtObservation=AllDimensions"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
   # print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        observations = data["dataSets"][0]["observations"]
        time_periods = data["structure"]["dimensions"]["observation"][7]["values"]
       # print(data)
        unemployment_data = []
        for key, values in observations.items():
            time_index = int(key.split(":")[-1])  # Último índice en la clave corresponde al tiempo
            unemployment_rate = values[0]  # El primer valor del array es el dato de desempleo
            date = time_periods[time_index]["id"]
            unemployment_data.append({"Fecha": date, "desempleo": unemployment_rate})

        unployment=pd.DataFrame(unemployment_data)
        return unployment
    else:
        return jsonify({"error": f"Error en la solicitud: {response.status_code}"}), response.status_code


