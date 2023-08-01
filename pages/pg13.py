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

dash.register_page(__name__, name='Queimadas Mapa SP')


def atualiza_fig():
    df=pd.DataFrame(columns={'estados','valor'})
    df['estados']=['SP']
    df['valor']=[1]

    ############ le o arquivo do brasil inteiro #############
    br=gpd.read_file('BR_UF_2022.shp')
    ######### escolhe o estado ########################
    br = br[br['SIGLA_UF'] == 'SP'].reset_index(drop=True)
    ########## transforma em formato geoson para o choropleth rodar #####
    br.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)

    rg=pd.read_excel('Queimada_SP.xlsx')  

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
                            size=rg['queimadas']*0.3),            
                            name='queimadas',
                            text=rg['geoName']))
    fig1.update_layout(paper_bgcolor='black', 
                   autosize=True,
                   hovermode='closest',  
                   width=600,height=600,
                   margin={"r":0,"t":0,"l":0,"b":0})
    return fig1
##########################################################################

def servidor_layout():
    return  html.Div(children=[
                    dbc.Container(dbc.Alert(html.H5("Queimadas estado: SP (últimos 7 dias)", 
                                            className="alert-heading"), color="info"),
                                            className="m-2"),
                    dcc.Graph(id='live-update-graph1',style={'width': '100%', 'height': '100%','display':'inline-block'},
                               figure = atualiza_fig()   ),              
                    ]) 

############### Passa o grafico dinamicamente para o Layout####################
layout = servidor_layout

