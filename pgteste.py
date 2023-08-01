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


kw_list=['febre','tosse','garganta','hospital']
#teste = pd.read_csv('dad1.txt', delimiter = "\t")
teste=pd.read_csv('dad1.txt', header=None)

teste['dias']=teste.index

peaks1, _ = find_peaks(teste[kw_list[0]], height=60)
peaks2, _ = find_peaks(teste[kw_list[1]], height=60)
peaks3, _ = find_peaks(teste[kw_list[2]], height=60)
peaks4, _ = find_peaks(teste[kw_list[3]], height=60)
#peaks, _ = find_peaks(teste['febre'], distance=4)

difer1=np.diff(peaks1)
difer2=np.diff(peaks2)
difer3=np.diff(peaks3)
difer4=np.diff(peaks4)

fig1 = px.line(teste,x='dias',y='febre')
fig1.add_trace(go.Scatter(x=teste.index[peaks1],
                          y=teste[kw_list[0]].values[peaks1],
                          mode='markers'))
fig1.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[0]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig1.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "febre"')

fig2 = px.histogram(difer1,nbins=5)
fig2.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas")


fig3 = px.line(difer1)
fig3.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução da distância entre picos"',
                   yaxis_title="distância horas")

fig4 = px.line(teste,x='dias',y='tosse')
fig4.add_trace(go.Scatter(x=teste.index[peaks2],
                          y=teste[kw_list[1]].values[peaks2],
                          mode='markers'))
fig4.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[1]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig4.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "tosse"')

fig5 = px.histogram(difer2,nbins=5)
fig5.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas")


fig6 = px.line(difer2)
fig6.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução-distância entre picos"',
                   yaxis_title="distância horas")


fig7 = px.line(teste,x='dias',y='garganta')
fig7.add_trace(go.Scatter(x=teste.index[peaks3],
                          y=teste[kw_list[2]].values[peaks3],
                          mode='markers'))
fig7.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[2]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig7.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "garganta"')

fig8 = px.histogram(difer3,nbins=5)
fig8.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas")


fig9 = px.line(difer3)
fig9.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução-distância entre picos"',
                   yaxis_title="distância horas")


fig10 = px.line(teste,x='dias',y='hospital')
fig10.add_trace(go.Scatter(x=teste.index[peaks4],
                          y=teste[kw_list[3]].values[peaks4],
                          mode='markers'))
fig10.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[3]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig10.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Busca no Google por "hospital"')

fig11 = px.histogram(difer4,nbins=5)
fig11.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Histograma-distância entre picos"',
                    xaxis_title="horas")


fig12 = px.line(difer4)
fig12.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Evolução-distância entre picos"',
                    yaxis_title="distância horas")

#df=pd.read_excel('Febre_norm.xlsx')
#df.drop(['febre_Google','febre_alta_Norm'],axis=1,inplace=True)

df=pd.DataFrame(columns=['febre_Google','febre_alta_Norm'])
df['febre_Google']=teste['febre']

z_normal=lambda x:(x-x.mean())/x.std()
teste=teste.apply(z_normal)

df['febre_alta_Norm']=teste['febre']

df.to_excel('gripe.xlsx')

