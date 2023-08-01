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


dash.register_page(__name__, name='Gripe Geral')


kw_list=['febre','tosse','garganta','hospital']
teste = pd.read_excel('google_febre.xlsx')
teste.set_index('date')
teste['dias']=teste.index

teste_t = pd.read_excel('google_tosse.xlsx')
teste['tosse']=teste_t['tosse'].values

teste_g = pd.read_excel('google_garganta.xlsx')
teste['garganta']=teste_g['garganta'].values

teste_h = pd.read_excel('google_hospital.xlsx')
teste['hospital']=teste_h['hospital'].values

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
                   title_text='Busca no Google por "febre"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)

fig2 = px.histogram(difer1,nbins=5)
fig2.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)


fig3 = px.line(difer1)
fig3.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução da distância entre picos"',
                   yaxis_title="distância horas",font=dict(size=9),autosize=True)

fig4 = px.line(teste,x='dias',y='tosse')
fig4.update_traces(line_color='yellow')
fig4.add_trace(go.Scatter(x=teste.index[peaks2],
                          y=teste[kw_list[1]].values[peaks2],
                          mode='markers'))
fig4.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[1]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig4.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "tosse"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)

fig5 = px.histogram(difer2,nbins=5,color_discrete_sequence = ['goldenrod'])
fig5.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)


fig6 = px.line(difer2)
fig6.update_traces(line_color='yellow')
fig6.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução-distância entre picos"',
                   yaxis_title="distância horas",font=dict(size=9),autosize=True)


fig7 = px.line(teste,x='dias',y='garganta')
fig7.update_traces(line_color='magenta')
fig7.add_trace(go.Scatter(x=teste.index[peaks3],
                          y=teste[kw_list[2]].values[peaks3],
                          mode='markers'))
fig7.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[2]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig7.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Busca no Google por "garganta"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)

fig8 = px.histogram(difer3,nbins=5,color_discrete_sequence = px.colors.sequential.Viridis)
fig8.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Histograma-distância entre picos"',
                   xaxis_title="horas",font=dict(size=9),autosize=True)


fig9 = px.line(difer3)
fig9.update_traces(line_color='magenta')
fig9.update_layout(template="plotly_dark",showlegend=False,
                   title_text='Evolução-distância entre picos"',
                   yaxis_title="distância horas",font=dict(size=9),autosize=True)


fig10 = px.line(teste,x='dias',y='hospital')
fig10.update_traces(line_color='white')
fig10.add_trace(go.Scatter(x=teste.index[peaks4],
                          y=teste[kw_list[3]].values[peaks4],
                          mode='markers'))
fig10.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[3]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
fig10.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Busca no Google por "hospital"',
                    xaxis_title="horas", font=dict(size=9),autosize=True)

fig11 = px.histogram(difer4,nbins=5,color_discrete_sequence = ['white'])
fig11.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Histograma-distância entre picos"',
                    xaxis_title="horas")


fig12 = px.line(difer4)
fig12.update_traces(line_color='white')
fig12.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Evolução-distância entre picos"',
                    yaxis_title="distância horas",font=dict(size=9),autosize=True)

df=pd.DataFrame(columns=['febre_Google','febre_alta_Norm'])
df['febre_Google']=teste['febre']

z_normal=lambda x:(x-x.mean())/x.std()
teste=teste.apply(z_normal)

df['febre_alta_Norm']=teste['febre']

df.to_excel('gripe.xlsx')



##########################################################################
layout = html.Div(children=[
    dbc.Container(dbc.Alert(html.H5("Situação de Gripe (últimos 7 dias)", className="alert-heading"), color="success"),
    className="m-2"),
    dcc.Graph(id='live-update-graph1',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig1),   
    dcc.Graph(id='live-update-graph2',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig2), 
    dcc.Graph(id='live-update-graph3',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig3), 
    dcc.Interval(
            id='interval-component1',
            interval=7*1000, # in milliseconds
            n_intervals=0), 
    html.Div(children=''),
    dcc.Graph(id='live-update-graph4',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig4),   
    dcc.Graph(id='live-update-graph5',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig5), 
    dcc.Graph(id='live-update-graph6',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig6), 
    dcc.Interval(
            id='interval-component2',
            interval=7*1000, # in milliseconds
            n_intervals=0),               
    html.Div(children=''),
    dcc.Graph(id='live-update-graph7',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig7),   
    dcc.Graph(id='live-update-graph8',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig8), 
    dcc.Graph(id='live-update-graph9',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig9), 
    dcc.Interval(             
            id='interval-component3',
            interval=7*1000, # in milliseconds
            n_intervals=0),               
    html.Div(children=''),              
    dcc.Graph(id='live-update-graph10',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig10),   
    dcc.Graph(id='live-update-graph11',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig11), 
    dcc.Graph(id='live-update-graph12',style={'width': '100%', 'height': '100%','display':'inline-block'},
       figure=fig12), 
    dcc.Interval(
            id='interval-component4',
            interval=7*1000, # in milliseconds
            n_intervals=0)               
])    

@callback(Output('live-update-graph10', 'figure'),
              Input('interval-component4', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live1(value):
        motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_hospital.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index

        peaks4, _ = find_peaks(teste[kw_list[3]], height=60)       
        fig10 = px.line(teste,x='dias',y='hospital')
        fig10.update_traces(line_color='white')
        fig10.add_trace(go.Scatter(x=teste.index[peaks4],
                          y=teste[kw_list[3]].values[peaks4],
                          mode='markers'))
        fig10.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[3]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
        fig10.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Busca no Google por "hospital"',xaxis_title="horas")
        return fig10

@callback(Output('live-update-graph11', 'figure'),
              Input('interval-component4', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live2(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_hospital.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks4, _ = find_peaks(teste[kw_list[3]], height=60)
        difer4=np.diff(peaks4)
        fig11 = px.histogram(difer4,nbins=5,color_discrete_sequence = ['white'])
        fig11.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Histograma-distância entre picos"',
                    xaxis_title="horas")
        return fig11
    
@callback(Output('live-update-graph12', 'figure'),
              Input('interval-component4', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live3(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_hospital.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks4, _ = find_peaks(teste[kw_list[3]], height=60)
        difer4=np.diff(peaks4)
        fig12 = px.line(difer4)
        fig12.update_traces(line_color='white')
        fig12.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Evolução-distância entre picos"',
                    yaxis_title="distância horas")
        return fig12

@callback(Output('live-update-graph7', 'figure'),
              Input('interval-component3', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live4(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_garganta.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index

        peaks3, _ = find_peaks(teste[kw_list[2]], height=60)       
        fig7 = px.line(teste,x='dias',y='garganta')
        fig7.update_traces(line_color='magenta')
        fig7.add_trace(go.Scatter(x=teste.index[peaks3],
                          y=teste[kw_list[2]].values[peaks3],
                          mode='markers'))
        fig7.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[2]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
        fig7.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Busca no Google por "garganta"',xaxis_title="horas")
        return fig7

@callback(Output('live-update-graph8', 'figure'),
              Input('interval-component3', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live5(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_garganta.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks3, _ = find_peaks(teste[kw_list[2]], height=60)
        difer3=np.diff(peaks3)
        fig8 = px.histogram(difer3,nbins=5,color_discrete_sequence = px.colors.sequential.Viridis)
        fig8.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Histograma-distância entre picos"',
                    xaxis_title="horas")
        return fig8
    
@callback(Output('live-update-graph9', 'figure'),
              Input('interval-component3', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live6(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_garaganta.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks3, _ = find_peaks(teste[kw_list[2]], height=60)
        difer3=np.diff(peaks3)
        fig9 = px.line(difer3)
        fig9.update_traces(line_color='magenta')
        fig9.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Evolução-distância entre picos"',
                    yaxis_title="distância horas")
        return fig9

@callback(Output('live-update-graph4', 'figure'),
              Input('interval-component2', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live7(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_tosse.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index

        peaks2, _ = find_peaks(teste[kw_list[1]], height=60)       
        fig4 = px.line(teste,x='dias',y='tosse')
        fig4.update_traces(line_color='yellow')
        fig4.add_trace(go.Scatter(x=teste.index[peaks2],
                          y=teste[kw_list[1]].values[peaks2],
                          mode='markers'))
        fig4.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[1]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
        fig4.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Busca no Google por "tosse"',xaxis_title="horas")
        return fig4

@callback(Output('live-update-graph5', 'figure'),
              Input('interval-component2', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live8(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_tosse.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks2, _ = find_peaks(teste[kw_list[1]], height=60)
        difer2=np.diff(peaks2)
        fig5 = px.histogram(difer2,nbins=5,color_discrete_sequence = ['goldenrod'])
        fig5.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Histograma-distância entre picos"',
                    xaxis_title="horas")
        return fig5
    
@callback(Output('live-update-graph6', 'figure'),
              Input('interval-component2', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live9(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_tosse.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks2, _ = find_peaks(teste[kw_list[1]], height=60)
        difer2=np.diff(peaks2)
        fig6 = px.line(difer2)
        fig6.update_traces(line_color='yellow')
        fig6.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Evolução-distância entre picos"',
                    yaxis_title="distância horas")
        return fig6

@callback(Output('live-update-graph1', 'figure'),
              Input('interval-component1', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live10(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_febre.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index

        peaks1, _ = find_peaks(teste[kw_list[0]], height=60)       
        fig1 = px.line(teste,x='dias',y='febre')
        fig1.add_trace(go.Scatter(x=teste.index[peaks1],
                          y=teste[kw_list[0]].values[peaks1],
                          mode='markers'))
        fig1.add_trace(go.Scatter(x=teste.index,
                          y=60*np.ones_like(teste[kw_list[0]].values),
                          line = dict(color='firebrick', width=4, dash='dot')
                          ))
        fig1.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Busca no Google por "febre"',xaxis_title="horas")
        return fig1

@callback(Output('live-update-graph2', 'figure'),
              Input('interval-component1', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live11(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_febre.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks1, _ = find_peaks(teste[kw_list[0]], height=60)
        difer1=np.diff(peaks1)
        fig2 = px.histogram(difer1,nbins=5)
        fig2.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Histograma-distância entre picos"',
                    xaxis_title="horas")
        return fig2
    
@callback(Output('live-update-graph3', 'figure'),
              Input('interval-component1', 'n_intervals'),
               prevent_initial_call=False)

def update_graph_live12(value):
        #motor.Ligar()
        kw_list=['febre','tosse','garganta','hospital']
        teste = pd.read_excel('google_febre.xlsx')
        teste.set_index('date')
        teste['dias']=teste.index
        peaks1, _ = find_peaks(teste[kw_list[0]], height=60)
        difer1=np.diff(peaks1)
        fig3 = px.line(difer1)
        fig3.update_layout(template="plotly_dark",showlegend=False,
                    title_text='Evolução-distância entre picos"',
                    yaxis_title="distância horas")
        return fig3

