import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Queimadas')

sidebar = dbc.Nav(
            [
                dbc.NavLink([html.Div("Queimadas Mapa SP", className="ms-2")],
                             href="/pg13", active="exact"),
                dbc.NavLink([html.Div("Queimadas Mapa RJ", className="ms-2")],
                             href="/pg14", active="exact"),
                dbc.NavLink([html.Div("Queimadas Mapa AM", className="ms-2")],
                             href="/pg15", active="exact"),   
                dbc.NavLink([html.Div("Queimadas Mapa PA", className="ms-2")],
                             href="/pg16", active="exact"),   
                dbc.NavLink([html.Div("Queimadas Mapa MT", className="ms-2")],
                             href="/pg17", active="exact"),  
                dbc.NavLink([html.Div("Queimadas Mapa TO", className="ms-2")],
                             href="/pg18", active="exact"),                               
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


