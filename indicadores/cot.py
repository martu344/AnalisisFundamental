from flask import Flask
import cot_reports as cot
import pandas as pd

app = Flask(__name__)

def get_cot_data(market):
    #llamado de datos
    df = pd.DataFrame()
    year=[2024,2025]
    df_list = []  # Lista para acumular los DataFrames
    for i in year:
       # print(i)
        single_year = pd.DataFrame(cot.cot_year(i, cot_report_type='traders_in_financial_futures_fut')) 
        df_list.append(single_year)  # Agregar cada DataFrame a la lista
    df = pd.concat(df_list, ignore_index=True)
    
    #suma total de open_interest
    mercado = "CHICAGO MERCANTILE EXCHANGE"
    filtroFecha=df['Market_and_Exchange_Names'] == market
    
    fechas = df.loc[filtroFecha,"Report_Date_as_YYYY-MM-DD"].values
    resultados = []
    for fecha in fechas:
        filtro = (df['Market_and_Exchange_Names'].str.contains(mercado, case=False)) & (df['Report_Date_as_YYYY-MM-DD'] == fecha)
        suma_fecha = df.loc[filtro, 'Open_Interest_All'].sum()
        resultados.append({"Fecha": fecha, "Interés Abierto Total": suma_fecha})
    open_interest_all = pd.DataFrame(resultados)
    #print(open_interest_all)
    cad = df[df['Market_and_Exchange_Names'] == market]
    cad=cad[["Report_Date_as_YYYY-MM-DD","Open_Interest_All","Pct_of_OI_Dealer_Long_All", "Pct_of_OI_Dealer_Short_All","Dealer_Positions_Long_All","Dealer_Positions_Short_All"]]
    
    Flow=[]
    Flow_total=[]
    monedas=[ {'label': 'Canadian Dollar', 'value': 'CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE'},
                {'label': 'Swiss Franc', 'value': "SWISS FRANC - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'British Pound', 'value': "BRITISH POUND - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Euro', 'value': "EURO FX - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Japanese Yen', 'value': "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Australian Dollar', 'value': "AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Mexican Peso', 'value':"MEXICAN PESO - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Brazilian Real', 'value': "BRAZILIAN REAL - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'NZ Dollar', 'value': "NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'So African Rand', 'value': "SO AFRICAN RAND - CHICAGO MERCANTILE EXCHANGE",}
                ]
    monedas=pd.DataFrame(monedas)
    for _,total in open_interest_all.iterrows():
        match = cad[total["Fecha"]==cad["Report_Date_as_YYYY-MM-DD"]]
        
        if not match.empty:
            porcentaje=(match["Open_Interest_All"].values[0]*100)/total["Interés Abierto Total"]
            pct_dealer_long=match["Pct_of_OI_Dealer_Long_All"].values[0]
            pct_dealer_short=match["Pct_of_OI_Dealer_Short_All"].values[0]
            #calculo metrica

            dealer_long=match["Dealer_Positions_Long_All"].values[0]
            dealer_short=match["Dealer_Positions_Short_All"].values[0]
            dealer_position_total=((dealer_short-dealer_long)/total["Interés Abierto Total"])*100
            Flow.append({"Fecha":total["Fecha"], "Pct_open_interes_all":porcentaje, "Pct_Long_dealers":pct_dealer_long, "Pct_Short_dealers":pct_dealer_short, "metrica":dealer_position_total })

            for q,idx in monedas.iterrows():
                    divisa = df[df['Market_and_Exchange_Names'] == idx["value"]]
                    divisa=divisa[["Report_Date_as_YYYY-MM-DD","Dealer_Positions_Long_All","Dealer_Positions_Short_All"]]
                    match2= divisa[total["Fecha"]==divisa["Report_Date_as_YYYY-MM-DD"]]
                    if not match2.empty:
                        dealer_long=match2["Dealer_Positions_Long_All"].values[0]
                        dealer_short=match2["Dealer_Positions_Short_All"].values[0]
                        dealer_position_total=((dealer_short-dealer_long)/total["Interés Abierto Total"])*100
                        Flow_total.append({"Fecha":total["Fecha"], "Divisa": idx["label"],"metrica":dealer_position_total })
            
            
    #print(pd.DataFrame(match))        
    Cad_Flow=pd.DataFrame(Flow)
    Cad_Flow.to_csv('Cad_Flow.csv', index=False)
    print(Cad_Flow)
    Divisas_Flow=pd.DataFrame(Flow_total)
    Divisas_Flow.to_csv('Divisas_Flow.csv', index=False)
    print(Divisas_Flow)   
    return Cad_Flow, Divisas_Flow