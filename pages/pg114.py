import matplotlib.pyplot as fig
from pytrends.request import TrendReq #precisa instalar essa biblioteca usando pip install
import matplotlib.dates as mdates
import pandas as pd
from scipy.signal import find_peaks
import numpy as np
import matplotlib.ticker as ticker
import plotly.express as px
from plotly.subplots import make_subplots
import dash
from dash import Dash, dcc, html, Input, Output,State,callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import geopandas as gpd
from geopy.geocoders import Nominatim
import json
import pyproj

dash.register_page(__name__, name='Desmatamento Mapa RS')

def atualiza_fig():
    df=pd.DataFrame(columns={'estados','valor'})
    df['estados']=['SP']
    df['valor']=[1]

    ############ le o arquivo do brasil inteiro #############
    br=gpd.read_file('BR_UF_2022.shp')
    ######### escolhe o estado ########################
    br = br[br['SIGLA_UF'] == 'RS'].reset_index(drop=True)
    ########## transforma em formato geoson para o choropleth rodar #####
    br.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)

    rg=pd.read_excel('Regiao_RS.xlsx')  

    ############ junta o dataframe especifico com o mapa da regiao #####
    merged = br.set_index('SIGLA_UF').join(df.set_index('estados'))

    ######### faz o mapa com choropleth ##################### 
    fig1 = px.choropleth(merged, geojson=merged.geometry, 
                    locations=merged.index)
    ########### centraliza o mapa na localizacao (estado ) #########
    fig1.update_geos(fitbounds = "locations", visible = False,bgcolor='black')

    fig1.add_trace(go.Scattergeo(visible=True,
                            lat=rg['latitude'],lon=rg['longitude'],
                            marker=dict(color='red',
                            colorscale='viridis',
                            size=rg['desmatamento']*0.3),            
                            name='desmatamento',
                            text=rg['geoName']))
    fig1.update_layout(paper_bgcolor='black', 
                   autosize=True,
                   hovermode='closest',  
                   width=600,height=600,
                   margin={"r":0,"t":0,"l":0,"b":0})
    return fig1

def atualiza_fig2():
    kwlist = ['desmatamento']
    data=pd.read_excel('Regiao_RS.xlsx')
    filtro = 35
    peaks, _ = find_peaks(data[kwlist[0]], height = filtro)

    picos = go.Figure()
# Linha principal
    picos.add_trace(go.Scatter(x=data.index,
                         y=data[kwlist[0]],
                         mode='lines',
                         name='Quantidade de busca',
                         line=dict(color='white')))
# Pontos de pico
    picos.add_trace(go.Scatter(x=data.index[peaks],
                         y=data[kwlist[0]].values[peaks],
                         mode='markers',
                         name='Picos de busca',
                         marker=dict(color='red', symbol='x')))
# Linha de filtro
    picos.add_trace(go.Scatter(x=data.index,
                         y=filtro * np.ones_like(data[kwlist[0]].values),
                        mode='lines',
                        name='Linha de Filtro',
                        line=dict(color='blue', dash='dash')))
# Configurando layout
    picos.update_layout(plot_bgcolor='black',
                  paper_bgcolor='black',
                  font=dict(color='white'),
                  showlegend=False,
                  title = 'Picos de busca na última semana',
                  xaxis=dict(showgrid=False),
                  yaxis=dict(showgrid=False))
    return picos

def atualiza_fig3():
    kwlist = ['desmatamento']
    dados=pd.read_excel('Regiao_RS.xlsx')
    filtro = 35

    peaks, _ = find_peaks(dados[kwlist[0]], height=filtro)
    difer = np.diff(peaks)
    grafico2 = px.histogram(x=difer, nbins=5, title='Frequência de buscas do termo "'+kwlist[0]+'" na última semana')
    grafico2.update_layout(template="plotly_dark",showlegend=False,
                           xaxis=dict(title='Quantidade de buscas'),
                           yaxis=dict(title='Frequência'),autosize=True)
    return grafico2

##########################################################################

def servidor_layout():
    return  html.Div(children=[
                    html.Div("designed by students Rodrigo Herrera, Pedro Perdomo", 
                             style={'fontSize':10, 'textAlign':'left',
                                                                    'font-weight': 'bold',
                                                                    'color':'white',
                                                                    'font-style':'italic'}),            
                    dbc.Container(dbc.Alert(html.H5("Desmatamento estado: RS (período 7 dias)", 
                                            className="alert-heading"), color="info"),
                                            className="m-2"),
                    dcc.Graph(id='live-update-graph1',style={'width': '100%', 'height': '100%','display':'inline-block'},
                               figure = atualiza_fig()   ), 
                    dcc.Graph(id='live-update-graph2',style={'width': '100%', 'height': '100%','display':'inline-block'},
                               figure = atualiza_fig2()   ), 
                    dcc.Graph(id='live-update-graph3',style={'width': '100%', 'height': '100%','display':'inline-block'},
                               figure = atualiza_fig3()   ),                               
                    ]) 

############### Passa o grafico dinamicamente para o Layout####################
layout = servidor_layout