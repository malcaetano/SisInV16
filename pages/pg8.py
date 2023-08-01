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
import motor


dash.register_page(__name__, name='Dengue Geral')

   

kw_list=['dengue']
teste = pd.read_excel('google_dengue.xlsx')
teste.set_index('date')
teste['horas']=teste.index

peaks1, _ = find_peaks(teste[kw_list[0]], height=30)
difer1=np.diff(peaks1)

fig1 = px.line(teste,x='horas',y='dengue')
fig1.update_traces(line_color='yellow')
fig1.add_trace(go.Scatter(x=teste.index[peaks1],
                          y=teste[kw_list[0]].values[peaks1],
                          mode='markers'
                          ))
fig1.add_trace(go.Scatter(x=teste.index,line_color='white',
                          y=30*np.ones_like(teste[kw_list[0]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig1.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "febre"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)

fig2 = px.histogram(difer1,nbins=5,color_discrete_sequence=['goldenrod'])
fig2.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)


fig3 = px.line(difer1)
fig3.update_traces(line_color='yellow')
fig3.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução da distância entre picos"',
                   yaxis_title="distância horas",font=dict(size=9),autosize=True)

##########################################################################
layout = html.Div(children=[
    dbc.Container(dbc.Alert(html.H5("Situação de Dengue (últimos 7 dias)", className="alert-heading"), color="info"),
    className="m-2"),
    dcc.Graph(id='live-update-graph1',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig1),   
    dcc.Graph(id='live-update-graph2',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig2), 
    dcc.Graph(id='live-update-graph3',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig3), 
])    
