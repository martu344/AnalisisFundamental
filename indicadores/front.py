import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import requests
import pandas as pd
import os

# Layout con varias páginas
layout = html.Div( style={
        'backgroundColor': 'black',  # Fondo azul oscuro opaco
        'color': 'white',             # Texto blanco para contraste
        'fontFamily': 'Arial',        # Cambiar la fuente
        'margin': '0',   # Sin margen
        'padding': '0',  # Sin relleno
        },
        children=[
    dcc.Location(id='url', refresh=False),  # Maneja la URL
    html.Div( style={
        'backgroundColor': 'black',  # Fondo azul oscuro opaco
        'color': 'white',             # Texto blanco para contraste
        'fontFamily': 'Arial',        # Cambiar la fuente
        },
        children=[
         html.Div(
            children=[
                dcc.Link('COT Data Viewer', href='/', className='custom-link'),
                dcc.Link('Indicadores', href='/page-2', className='custom-link'),
                dcc.Link('Correlacion', href='/page-3', className='custom-link'),
            ],
            className='link-container',
        ),
    ]),
    html.Div(id='page-content'),  # Aquí se actualizará el contenido dependiendo de la ruta
])

def page_1():
    return html.Div([
        html.H1("COT Data Viewer",                   
                 style={
                    'textAlign': 'center',  # Centrar el encabezado
                    'color': 'white',       # Texto blanco
                    'fontSize': '36px',     # Tamaño del texto
                    'fontWeight': 'bold'    # Negrita
            }),
        dcc.Dropdown(
            id='market-dropdown',
            options=[
                {'label': 'Canadian Dollar', 'value': 'CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE'},
                {'label': 'Swiss Franc', 'value': "SWISS FRANC - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'British Pound', 'value': "BRITISH POUND - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Euro', 'value': "EURO FX - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Japanese Yen', 'value': "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Australian Dollar', 'value': "AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Mexican Peso', 'value':"MEXICAN PESO - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'Brazilian Real', 'value': "BRAZILIAN REAL - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'NZ Dollar', 'value': "NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE"},
                {'label': 'So African Rand', 'value': "SO AFRICAN RAND - CHICAGO MERCANTILE EXCHANGE",},
                {'label': "USD INDEX", 'value': "USD INDEX - ICE FUTURES U.S."},
            ],
            value='CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE',
            placeholder="Selecciona una moneda",
             style={
                    'width': '200px',         # Más corto
                    'margin': '0 15px',       # Centrado horizontalmente
                    'backgroundColor': 'black',  # Fondo negro
                    'color': 'white',         # Texto blanco
                    'borderRadius': '5px',   # Bordes redondeados
                    'fontSize': '14px',      # Tamaño de fuente
                    }
        ),
        dcc.Graph(id='cot-graph'),
        dcc.Graph(id='long-short-graph'),
        dcc.Dropdown(
            id='market-dropdown2',
            options=[
                {'label': 'Canadian Dollar', 'value': 'Canadian Dollar'},
                {'label': 'Swiss Franc', 'value': "Swiss Franc"},
                {'label': 'British Pound', 'value': "British Pound"},
                {'label': 'Euro', 'value': "Euro"},
                {'label': 'Japanese Yen', 'value': "Japanese Yen"},
                {'label': 'Australian Dollar', 'value': "Australian Dollar"},
                {'label': 'Mexican Peso', 'value':"Mexican Peso"},
                {'label': 'Brazilian Real', 'value': "Brazilian Real"},
                {'label': 'NZ Dollar', 'value': "NZ Dollar"},
                {'label': 'So African Rand', 'value': "So African Rand",},
            ],
            value='Canadian Dollar',
            placeholder="Selecciona una moneda",
             style={
                    'width': '200px',         # Más corto
                    'margin': '0 15px',       # Centrado horizontalmente
                    'backgroundColor': 'black',  # Fondo negro
                    'color': 'white',         # Texto blanco
                    'borderRadius': '5px',   # Bordes redondeados
                    'fontSize': '14px',      # Tamaño de fuente
                    }
        ),
        dcc.Dropdown(
            id='market-dropdown3',
            options=[
                {'label': 'Canadian Dollar', 'value': 'Canadian Dollar'},
                {'label': 'Swiss Franc', 'value': "Swiss Franc"},
                {'label': 'British Pound', 'value': "British Pound"},
                {'label': 'Euro', 'value': "Euro"},
                {'label': 'Japanese Yen', 'value': "Japanese Yen"},
                {'label': 'Australian Dollar', 'value': "Australian Dollar"},
                {'label': 'Mexican Peso', 'value':"Mexican Peso"},
                {'label': 'Brazilian Real', 'value': "Brazilian Real"},
                {'label': 'NZ Dollar', 'value': "NZ Dollar"},
                {'label': 'So African Rand', 'value': "So African Rand",},
            ],
            value='Canadian Dollar',
            placeholder="Selecciona una moneda",
             style={
                    'width': '200px',         # Más corto
                    'margin': '0 15px',       # Centrado horizontalmente
                    'backgroundColor': 'black',  # Fondo negro
                    'color': 'white',         # Texto blanco
                    'borderRadius': '5px',   # Bordes redondeados
                    'fontSize': '14px',      # Tamaño de fuente
                    }
        ),
        dcc.Graph(id='metrica-graph'),
        dcc.Graph(id='metrica-total-graph'),
    ])

def page_2():
    return html.Div([
        html.H1("Indicadores Economicos",                    
                style={
                    'textAlign': 'center',  # Centrar el encabezado
                    'color': 'white',       # Texto blanco
                    'fontSize': '36px',     # Tamaño del texto
                    'fontWeight': 'bold'    # Negrita
            }), 
        dcc.Dropdown(
            id='indicadores',
            options=[
                {'label': 'Canadian Dollar', 'value': 'CAN'},
                {'label': 'Swiss Franc', 'value': "SWE"},
                {'label': 'British Pound', 'value': "GBR"},
                {'label': 'Euro', 'value': "EA20"},
                {'label': 'Japanese Yen', 'value': "JPN"},
                {'label': 'Australian Dollar', 'value': "AUS"},
                {'label': 'Mexican Peso', 'value':"MEX"},
                {'label': 'NZ Dollar', 'value': "NZL"},
                {'label': 'So African Rand', 'value': "ZAF",},
                {'label': "USD INDEX", 'value': "USA"},
            ],
            value='CAN',
            placeholder="Selecciona una divisa ",
             style={
                    'width': '200px',         # Más corto
                    'margin': '0 15px',       # Centrado horizontalmente
                    'backgroundColor': 'black',  # Fondo negro
                    'color': 'white',         # Texto blanco
                    'borderRadius': '5px',   # Bordes redondeados
                    'fontSize': '14px',      # Tamaño de fuente
                    }
        ),
        dcc.Graph(id='unemployment-graph'),
        dcc.Graph(id='sentimiento-graph'),
        dcc.Graph(id='cpi-graph'),
        dcc.Graph(id='tasas-graph'),
        dcc.Graph(id='pib-graph')
    ])

def page_3():
    return html.Div(    
        style={
        'backgroundColor': 'black',  # Fondo azul oscuro opaco
        'color': 'white',             # Texto blanco para contraste
        'fontFamily': 'Arial',        # Cambiar la fuente
        'padding': '20px'             # Añadir espacio alrededor de la página
        },
        children=[
            html.H1("Correlaciones",            
                    style={
                    'textAlign': 'center',  # Centrar el encabezado
                    'color': 'white',       # Texto blanco
                    'fontSize': '36px',     # Tamaño del texto
                    'fontWeight': 'bold'    # Negrita
            }), 
            html.Button("Actualizar", id="load-data-btn", n_clicks=0, style={'margin': '10px'}),
            dash_table.DataTable(
                id='correlation-table',
                columns=[],  # Las columnas se definirán dinámicamente
                data=[],     # Los datos se cargarán dinámicamente
                style_table={'overflowX': 'auto', 
                             'margin': '20px',
                             'height': '400px',
                             'overflowY': 'auto'
                             },
                style_cell={'backgroundColor': 'black',
                            'textAlign': 'center',
                            'padding': '10px',
                            'fontSize': '14px',  # Cambia el tamaño del texto
                            'fontFamily': 'Arial',  # Cambia la fuente (opcional)
                            'color': 'lightgray', 
                            },
                style_header={'backgroundColor': 'darkblue', 
                              'fontWeight': 'bold',
                              'position': 'sticky',
                              'top': 0, 
                              'zIndex': 2}, 
                style_cell_conditional=[
                {
                    'if': {'column_id': 'Symbol'},
                    'position': 'sticky',
                    'left': 0,
                    'backgroundColor': 'darkblue',
                    'zIndex': 1  # Asegura que esté visible cuando se solapen otras celdas
                }
            ]), 
            dash_table.DataTable(
                id='correlation-table2',
                columns=[],  # Las columnas se definirán dinámicamente
                data=[],     # Los datos se cargarán dinámicamente
                style_table={'overflowX': 'auto',
                              'margin': '20px',
                              'height': '400px',
                              'overflowY': 'auto'
                              },
                style_cell={'backgroundColor': 'black',
                            'textAlign': 'center',
                            'padding': '10px',
                            'fontSize': '14px',  # Cambia el tamaño del texto
                            'fontFamily': 'Arial',  # Cambia la fuente (opcional)
                            'color': 'lightgray', 
                            },
                style_header={'backgroundColor': 'darkblue',
                              'fontWeight': 'bold',
                              'position': 'sticky',
                              'top': 0, 
                              'zIndex': 2}, 
                style_cell_conditional=[
                {
                    'if': {'column_id': 'Symbol'},
                    'position': 'sticky',
                    'left': 0,
                    'backgroundColor': 'darkblue',
                    'zIndex': 1  # Asegura que esté visible cuando se solapen otras celdas
                }
            ])
        ])


# Callback para cambiar el contenido de la página basado en la URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/page-2':  # Cuando la URL sea '/page-2'
        return page_2()
    if pathname == "/page-3":
        return page_3()
    # Página principal por defecto
    return page_1()

#render correlacion
@app.callback(
        [Output('correlation-table', 'columns'),
        Output('correlation-table', 'data'),
        Output('correlation-table2', 'columns'),
        Output('correlation-table2', 'data')],
        [Input('load-data-btn', 'n_clicks'),
        Input('url', 'pathname')])
def update_correlacion_table(n_clicks, pathname):
    if pathname != '/page-3':
        return dash.no_update
    if n_clicks > 0:
        if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
            url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/correlacion-data"
        else:
            # Esto es para cuando está localmente
            url = f"http://127.0.0.1:5000/correlacion-data"
        response = requests.get(url)
        if response.status_code != 200:
            return {
                'data': [],
                'layout': {'title': f'Error al cargar los datos de correlacion'}
            }
        data = response.json()
        df_filtrada = data["filtrada"]
        df_completa= data["completa"]
        df_completa = pd.DataFrame(df_completa)
        df_filtrada = pd.DataFrame(df_filtrada)
        #ordenamos los symbols
        desired_order = ['Symbol'] + [col for col in df_filtrada.columns if col not in ['Symbol']]
        df_filtrada = df_filtrada[desired_order]
        desired_order = ['Symbol'] + [col for col in df_completa.columns if col not in ['Symbol']]
        df_completa = df_completa[desired_order]
        #creamos las columnas para la tabla
        columns = [{'name': col, 'id': col} for col in df_filtrada.columns]
        df_filtrada = df_filtrada.to_dict('records')  # Convierte el DataFrame a una lista de registros
        columnsCompleta = [{'name': col, 'id': col} for col in df_completa.columns]
        df_completa = df_completa.to_dict('records')  # Convierte el DataFrame a una lista de registros

        return columns, df_filtrada, columnsCompleta, df_completa
    return dash.no_update
#render desempleo
@app.callback(
    Output('unemployment-graph', 'figure'),
    [Input('url', 'pathname'),
     Input("indicadores","value")]
)
def update_unemployment_graph(pathname,selected_market):
    if pathname != '/page-2':
        return dash.no_update
    if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
        url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/desempleo-data?market={selected_market}"
    else:
        # Esto es para cuando está localmente
        url = f"http://127.0.0.1:5000/desempleo-data?market={selected_market}"
    response = requests.get(url)
    if response.status_code != 200:
        return {
            'data': [],
            'layout': {'title': f'Error al cargar los datos de desempleo de {selected_market}'}
        }

    data = pd.DataFrame(response.json())
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data = data.sort_values(by='Fecha')

    return {
        'data': [
            {'x': data['Fecha'], 'y': data['desempleo'], 'type': 'line','line': {'color': 'blue'}, 'name': 'Tasa de Desempleo'},
        ],
        'layout': {
            'title': {
                'text':  f'Tasa de Desempleo de {selected_market}',
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        }
    }

#render cpi
@app.callback(
    Output('cpi-graph', 'figure'),
    [Input('url', 'pathname'),
     Input("indicadores","value")]
)
def update_cpi_graph(pathname,selected_market):
    if pathname != '/page-2':
        return dash.no_update
    if not selected_market:  # Si no hay selección, no hace nada
        return dash.no_update, dash.no_update
    if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
        url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/cpi-data?market={selected_market}"
    else:
        # Esto es para cuando está localmente
        url = f"http://127.0.0.1:5000/cpi-data?market={selected_market}"
    response = requests.get(url)
    if response.status_code != 200:
        return {
            'data': [],
            'layout': {'title': f'Error al cargar los datos de CPI de {selected_market}'}
        }

    data = pd.DataFrame(response.json())
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data = data.sort_values(by='Fecha')

    return {
        'data': [
            {'x': data['Fecha'], 'y': data['CPI'], 'type': 'line','line': {'color': 'blue'}, 'name': 'CPI'},
        ],
        'layout': {
            'title': {
                'text':  f'CPI de {selected_market}',
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        }
    }

#render sentimento
@app.callback(
    Output('sentimiento-graph', 'figure'),
    [Input('url', 'pathname'),
     Input("indicadores","value")]
)
def update_sentimiento_graph(pathname,selected_market):
    if pathname != '/page-2':
        return dash.no_update
    if not selected_market:  # Si no hay selección, no hace nada
        return dash.no_update, dash.no_update
    if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
        url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/sentimiento-data?market={selected_market}"
    else:
        # Esto es para cuando está localmente
        url = f"http://127.0.0.1:5000/sentimiento-data?market={selected_market}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {
            'data': [],
            'layout': {'title': f'Error al cargar los datos de Sentimiento del consumidor de {selected_market}'}
        }

    data = pd.DataFrame(response.json())
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data = data.sort_values(by='Fecha')

    return {
        'data': [
            {'x': data['Fecha'], 'y': data['sentimiento'], 'type': 'line','line': {'color': 'blue'}, 'name': 'sentimiento'},
        ],
        'layout': {
            'title': {
                'text':  f'Sentimiento del consumidor de {selected_market}',
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        }
    }

#render tasas
@app.callback(
    Output('tasas-graph', 'figure'),
    [Input('url', 'pathname'),
     Input("indicadores","value")]
)
def update_tasas_graph(pathname,selected_market):
    if pathname != '/page-2':
        return dash.no_update
    if not selected_market:  # Si no hay selección, no hace nada
        return dash.no_update, dash.no_update
    if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
        url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/tasas-data?market={selected_market}"
    else:
        # Esto es para cuando está localmente
        url = f"http://127.0.0.1:5000/tasas-data?market={selected_market}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {
            'data': [],
            'layout': {'title': f'Error al cargar los datos de Tasas de Interes de {selected_market}'}
        }

    data = pd.DataFrame(response.json())
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data = data.sort_values(by='Fecha')

    return {
        'data': [
            {'x': data['Fecha'], 'y': data['Tasa'], 'type': 'line','line': {'color': 'blue'}, 'name': 'tasas'},
        ],
         'layout': {
            'title': {
                'text':  f'Tasas de Interes de {selected_market}',
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        }
    }

#render PIB
@app.callback(
    Output('pib-graph', 'figure'),
    [Input('url', 'pathname'),
     Input("indicadores","value")]
)
def update_pib_graph(pathname,selected_market):
    if pathname != '/page-2':
        return dash.no_update
    if not selected_market:  # Si no hay selección, no hace nada
        return dash.no_update, dash.no_update
    if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
        url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/pib-data?market={selected_market}"
    else:
        # Esto es para cuando está localmente
        url = f"http://127.0.0.1:5000/pib-data?market={selected_market}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {
            'data': [],
            'layout': {'title': f'Error al cargar los datos de PIB de {selected_market}'}
        }

    data = pd.DataFrame(response.json())
    data['Fecha'] = pd.to_datetime(data['Fecha'])
    data = data.sort_values(by='Fecha')

    return {
        'data': [
            {'x': data['Fecha'], 'y': data['Tasa'], 'type': 'line','line': {'color': 'blue'}, 'name': 'pib'},
        ],
        'layout': {
            'title': {
                'text':  f'PIB de {selected_market}',
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        }
    }

# render COT
@app.callback(
    [Output('cot-graph', 'figure'),
     Output('long-short-graph', 'figure'),
     Output('metrica-graph', 'figure'),
     Output('metrica-total-graph', 'figure')],
    [Input('market-dropdown', 'value'),
     Input('market-dropdown2', 'value'),
     Input('market-dropdown3', 'value')]
)
def update_graphs(selected_market,selected_market2,selected_market3):
    if not selected_market:  # Si no hay selección, no hace nada
        return dash.no_update, dash.no_update
    if os.environ.get('RENDER_EXTERNAL_URL'):
        # Esto es para cuando está en Render
        url = f"{os.environ.get('RENDER_EXTERNAL_URL')}/cot-data?market={selected_market}"
    else:
        # Esto es para cuando está localmente
        url = f"http://127.0.0.1:5000/cot-data?market={selected_market}"
    
    response = requests.get(url)
    data = response.json()
    df_filtrada = data["filtrada"]
    df_completa= data["completa"]
    df_completa = pd.DataFrame(df_completa)
    df_filtrada = pd.DataFrame(df_filtrada)

    df_filtrada['Fecha'] = pd.to_datetime(df_filtrada['Fecha'])
    df_filtrada = df_filtrada.sort_values(by='Fecha')

    df_completa['Fecha'] = pd.to_datetime(df_completa['Fecha'])
    df_completa = df_completa.sort_values(by='Fecha')

    fig1 = {
        'data': [
            {'x': df_filtrada['Fecha'], 'y': df_filtrada['Pct_open_interes_all'], 'type': 'line', 'line': {'color': 'blue'}, 'name': 'Pct_open_interes_all'},
        ],
        'layout': {
            'title': {
                'text': f"Open Interest for {selected_market}",
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        }
    }

    fig2 = {
        'data': [
            {'x': df_filtrada['Fecha'], 'y': df_filtrada['Pct_Long_dealers'], 'type': 'line','line': {'color': 'blue'} ,'name': 'Pct_Long_dealers'},
            {'x': df_filtrada['Fecha'], 'y': df_filtrada['Pct_Short_dealers'], 'type': 'line','line': {'color': 'yellow'}, 'name': 'Pct_Short_dealers'},
        ],
        'layout': {
            'title': {
                'text': f"Long/Short Dealers for {selected_market}",
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        },
    }
    if not selected_market2:  # Si no hay selección, no hace nada
        return dash.no_update, dash.no_update
    df_2 = df_completa[df_completa['Divisa'] == selected_market2]
    df_1 = df_completa[df_completa['Divisa'] == selected_market3]

    # Ordenar por fecha para asegurar que los cálculos se hagan en orden cronológico
    df_2 = df_2.sort_values(by='Fecha')
    df_1 = df_1.sort_values(by='Fecha')

    df_pivot = df_completa.pivot(index="Fecha", columns="Divisa", values="metrica").reset_index()

    # Calcular la diferencia entre las métricas del Euro y el Canadian Dollar
    df_pivot["Diferencia_Euro_Canadian"] = df_pivot[selected_market3] - df_pivot[selected_market2]

    # Calcular la diferencia porcentual semanal para el Euro
    df_2["Cambio_Absoluto"] = df_2["metrica"].diff()
    df_2["Diferencia_Porcentual"] = (df_2["Cambio_Absoluto"] / abs(df_2["metrica"].shift(1))) * 100
    #df_euro['Diferencia_Porcentual'] = df_euro['metrica'].pct_change() * 100

    # Calcular la diferencia porcentual semanal para el Canadian Dollar
    df_1["Cambio_Absoluto"] = df_1["metrica"].diff()
    df_1["Diferencia_Porcentual"] = (df_1["Cambio_Absoluto"] / abs(df_1["metrica"].shift(1))) * 100
    #df_cad['Diferencia_Porcentual'] = df_cad['metrica'].pct_change() * 100
    fig3 = {
        'data': [
            {'x': df_pivot['Fecha'], 'y': df_pivot['Diferencia_Euro_Canadian'], 'type': 'line','line': {'color': 'blue'} ,'name': 'Euro'},
            #{'x': df_cad['Fecha'], 'y': df_cad['Diferencia_Porcentual'], 'type': 'line','line': {'color': 'white'} ,'name': 'CAD'}
        ],
        'layout': {
            'title': {
                'text': f"Diferencia entre {selected_market2} and {selected_market3}",
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        },
    }
    colores = {
    'Canadian Dollar': 'white',
    'Swiss Franc': 'green',
    'British Pound': 'red',
    'Euro': 'purple',
    'Japanese Yen': 'orange',
    'Australian Dollar': 'brown',
    'Mexican Peso': 'pink',
    'Brazilian Real': 'yellow',
    'NZ Dollar': 'cyan',
    'So African Rand': 'magenta'
    }
    fig4 = {
        'data': [
            {
                'x': df_completa[df_completa['Divisa'] == selected_market2]['Fecha'],
                'y': df_completa[df_completa['Divisa'] == selected_market2]['metrica'],
                'type': 'line',
                'line':{'color': colores.get(selected_market2, 'blue')},
                'name': selected_market2
            },{
                'x': df_completa[df_completa['Divisa'] == selected_market3]['Fecha'],
                'y': df_completa[df_completa['Divisa'] == selected_market3]['metrica'],
                'type': 'line',
                'line':{'color': colores.get(selected_market3, 'blue')},
                'name': selected_market3
            }
        ],
        'layout': {
            'title': {
                'text': f"Metrica for {selected_market2} and {selected_market3}",
                'font': {'color': 'white'}  # Texto blanco en el título
            },
            'plot_bgcolor': 'black',  # Fondo negro del gráfico
            'paper_bgcolor': 'black',  # Fondo negro alrededor del gráfico
            'font': {'color': 'white'},  # Texto blanco general
            'xaxis': {
                'title': 'Eje X',
                'color': 'white',  # Texto blanco en los ejes
                'gridcolor': 'gray',  # Líneas de rejilla en gris
            },
            'yaxis': {
                'title': 'Eje Y',
                'color': 'white',
                'gridcolor': 'gray',
            },
        },
    }
    return fig1, fig2, fig3, fig4

if __name__ == '__main__':
    app.run_server(debug=True)
