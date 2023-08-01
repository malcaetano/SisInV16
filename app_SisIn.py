import dash
from dash import html, dcc
from dash import Dash, dcc, html, Input, Output,State
import dash_bootstrap_components as dbc
import motor
import base64

dbc_css="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/cyborg/bootstrap.min.css"
#app = Dash(__name__,external_stylesheets=[dbc_css])

app = dash.Dash(__name__, use_pages=True,external_stylesheets=[dbc_css] )

############### liga o motor do Goolge ###########
#motor.Ligar()
##################################################


    
sidebar = dbc.Nav(
            [
                dbc.NavLink([html.Div("Home",className="ms-2")],
                             href="/", active="exact"),
                dbc.NavLink([html.Div("Chuvas Extremas", className="ms-2")],
                             href="/pg2", active="exact"),
                dbc.NavLink([html.Div("Gripe",className="ms-2")],
                             href="/pg4", active="exact"),
                dbc.NavLink([html.Div("Dengue",className="ms-2")],
                             href="/pg7", active="exact"),     
                dbc.NavLink([html.Div("Desmatamento",className="ms-2")],
                             href="/pg9", active="exact"),
                dbc.NavLink([html.Div("Queimadas",className="ms-2")],
                             href="/pg12", active="exact")                              
             ],   
            vertical=True,
            pills=True,
            className="bg-light",
)

image_filename = 'Logo_Insper.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
                
app.layout = html.Div(
       
    [ 
      dbc.Row([
     dbc.Col([
     html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
              style={'height':'10vh','width':'10vh'})
             ],width={'size':1,'offset':0,'order':'1'}),
     dbc.Col([
      dbc.Container(dbc.Alert(html.H5("SisIn", style={'fontSize':70, 'textAlign':'center'},
                        className="alert-heading"), color="primary"),
          className="m-2"),
            ],width={'size':5,'offset':1,'order':'1'}),
       ]),
       html.Div("designed by Prof. Dr. Marco A. L. Caetano", style={'fontSize':12, 'textAlign':'left',
                                                                    'font-weight': 'bold',
                                                                    'color':'white',
                                                                    'font-style':'italic'}),
       html.Hr(),
        html.Div("Eventos Extremos", style={'fontSize':30, 'textAlign':'left'}),

    dbc.Row(
        [
            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10),

            dbc.Col(
                [
                    
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2 )
        ]
    ),
        html.Hr(),
    ]
)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False,port=8080)
    
