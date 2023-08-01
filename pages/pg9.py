import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Desmatamento')

sidebar = dbc.Nav(
            [
                dbc.NavLink([html.Div("Desmatamento Geral", className="ms-2")],
                             href="/pg10", active="exact"),
                dbc.NavLink([html.Div("Desmatamento Mapa PA", className="ms-2")],
                             href="/pg11", active="exact"),  
                dbc.NavLink([html.Div("Desmatamento Mapa PR", className="ms-2")],
                             href="/pg112", active="exact"), 
                dbc.NavLink([html.Div("Desmatamento Mapa SP", className="ms-2")],
                             href="/pg113", active="exact"), 
                dbc.NavLink([html.Div("Desmatamento Mapa RS", className="ms-2")],
                             href="/pg114", active="exact"),   
                dbc.NavLink([html.Div("Desmatamento Mapa MG", className="ms-2")],
                             href="/pg115", active="exact"),
                dbc.NavLink([html.Div("Desmatamento Mapa AM", className="ms-2")],
                             href="/pg116", active="exact")                             
             ],   
            vertical=True,
            pills=True,
            className="bg-light",
)
                
layout = html.Div(
       
    [     
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

      ]
    ),
        html.Hr(),   
    ]
)


