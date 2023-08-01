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

dash.register_page(__name__, name='Desmatamento Mapa SP')

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

    rg=pd.read_excel('Regiao_SP.xlsx')  

    ############ junta o dataframe especifico com o mapa da regiao #####
    merged = br.set_index('SIGLA_UF').join(df.set_index('estados'))

    ######### faz o mapa com choropleth ##################### 
    fig1 = px.choropleth(merged,
                   geojson=merged.geometry,
                   locations=merged.index,
                   projection="mercator")
    ########### centraliza o mapa na localizacao (estado ) #########
    fig1.update_geos(fitbounds = "locations", visible = False,bgcolor='black')
    fig1.add_trace(px.scatter_geo(rg, lat='latitude', 
                                  lon='longitude', 
                                  size='desmatamento', 
                                  color='desmatamento', 
                                  hover_data=['geoName','desmatamento']).data[0]) 
    fig1.update_layout(paper_bgcolor='black', 
                   autosize=True,
                   hovermode='closest',  
                   width=350,height=350,
                   margin={"r":0,"t":0,"l":0,"b":0})
    fig1.update_layout(showlegend=False)
    return fig1

def atualiza_fig2():
    kw_list = ['desmatamento']
    interesse=pd.read_excel('Regiao_SP.xlsx')
    altura_pico = 40

    peaks, _ = find_peaks(interesse[kw_list[0]], height=altura_pico)

    grafico1 = px.line(interesse, x=interesse.index, y=kw_list[0], title='Picos Relevantes')
    grafico1.add_scatter(x=interesse.index[peaks], y=interesse[kw_list[0]].values[peaks], mode='markers', name='Peaks')
    grafico1.add_shape(type='line', x0=interesse.index[0], x1=interesse.index[-1], y0=altura_pico, y1=altura_pico,
              line=dict(dash='dash', color='red'), name='Peak Height')
    grafico1.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "desmatamento"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)
    return grafico1

def atualiza_fig3():
    kw_list = ['desmatamento']
    interesse=pd.read_excel('Regiao_SP.xlsx')
    altura_pico = 25

    peaks, _ = find_peaks(interesse[kw_list[0]], height=altura_pico)
    difer = np.diff(peaks)
    grafico2 = px.histogram(x=difer, nbins=5, title='Histograma das Distâncias entre os picos')
    grafico2.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)
    return grafico2

##########################################################################

def servidor_layout():
    return  html.Div(children=[
                    dbc.Container(dbc.Alert(html.H5("Desmatamento estado: SP (período 7 dias)", 
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