from flask import Flask, jsonify, request
from .desempleo import get_desempleo_data
from .cot import get_cot_data
from .cpi import get_cpi_data
from .tasas_de_interes import get_tasas_data
from .consumidor import get_sentimiento_data
from .pib import get_pib_data
from .script import get_correlacion_data
import pandas as pd
from .front import page_1
import os

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

#@app.route('/')
#def page():
#    return page_1()

# Ruta CPI
@app.route('/cpi-data', methods=['GET'])
def cpi_data():
    market = request.args.get('market', 'CAN')
    try:
        data = get_cpi_data(market)
        return data.to_json(orient='records')  # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta COT
@app.route('/cot-data', methods=['GET'])
def cot_data():
    market = request.args.get('market', 'CANADIAN DOLLAR')
    try:
        data_cot, data_total = get_cot_data(market)
        data = {
                'filtrada': data_cot.to_dict(orient='records'),
                'completa': data_total.to_dict(orient='records')
                }
        return data # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#Ruta Desempleo
@app.route('/desempleo-data', methods=['GET'])
def desempleo_data():
    market = request.args.get('market', 'CAN')
    try:
        data = get_desempleo_data(market)
        return data.to_json(orient='records')  # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#Ruta Tasas
@app.route('/tasas-data', methods=['GET'])
def tasas_data():
    market = request.args.get('market', 'CAN')
    try:
        data = get_tasas_data(market)
        return data.to_json(orient='records')  # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
#Ruta Sentimiento
@app.route('/sentimiento-data', methods=['GET'])
def sentimiento_data():    
    market = request.args.get('market', 'CAN')
    try:
        data = get_sentimiento_data(market)
        return data.to_json(orient='records')  # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#Ruta Pib
@app.route('/pib-data', methods=['GET'])
def pib_data():    
    market = request.args.get('market', 'CAN')
    try:
        data = get_pib_data(market)
        return data.to_json(orient='records')  # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#Ruta correlacion
@app.route('/correlacion-data', methods=['GET'])
def correlacion_data():    
    try:
        dataFiltrada, dataCompleta = get_correlacion_data()
        
        data = {
                'filtrada': dataFiltrada.to_dict(orient='records'),
                'completa': dataCompleta.to_dict(orient='records')
                }
        return jsonify(data)  # Devuelve los datos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400
          
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

#cad_porcentajeInteresAbierto= cad["Open_Interest_All"] 
#cad_porcentajeLargos= cad["Pct_of_OI_Dealer_Long_All"]
#cad_porcentajeCortos= cad["Pct_of_OI_Dealer_Short_All"]
#cad4_porcentajeInteresAbierto= cad["Report_Date_as_YYYY-MM-DD"]




#print(cad_porcentajeInteresAbierto)

#Pct_of_Open_Interest_All: Porcentaje del interés abierto total. de cada moneda con esto puedo medir el flujo de dinero
#Pct_of_OI_Dealer_Long_All: Porcentaje de las posiciones largas de dealers sobre el interés abierto.
#Pct_of_OI_Dealer_Short_All: Porcentaje de las posiciones cortas de dealers sobre el interés abierto.
#Pct_of_OI_Lev_Money_Long_All: Porcentaje de las posiciones largas de dinero apalancado sobre el interés abierto.
#Pct_of_OI_Lev_Money_Short_All: Porcentaje de las posiciones cortas de dinero apalancado sobre el interés abierto.

#Change_in_Open_Interest_All: Cambio en el interés abierto total.
#Change_in_Dealer_Long_All: Cambio en las posiciones largas de dealers.
#Change_in_Dealer_Short_All: Cambio en las posiciones cortas de dealers.
#Change_in_Lev_Money_Long_All: Cambio en las posiciones largas de dinero apalancado.
#Change_in_Lev_Money_Short_All: Cambio en las posiciones cortas de dinero apalancado

#Dealers (comercializadores o hedgers)
#Dealer_Positions_Long_All: Posiciones largas (compras) de dealers.
#Dealer_Positions_Short_All: Posiciones cortas (ventas) de dealers.
#Asset Managers (gestores de activos)
#Asset_Mgr_Positions_Long_All: Posiciones largas de gestores de activos.
#Asset_Mgr_Positions_Short_All: Posiciones cortas de gestores de activos.
#Leveraged Money (dinero apalancado o especuladores)
#Lev_Money_Positions_Long_All: Posiciones largas de traders apalancados.
#Lev_Money_Positions_Short_All: Posiciones cortas de traders apalancados.
#Other Reportables (otros reportables)
#Other_Rept_Positions_Long_All: Posiciones largas de otros traders reportables.
#Other_Rept_Positions_Short_All: Posiciones cortas de otros traders reportables.
