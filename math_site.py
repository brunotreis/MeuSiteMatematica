from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State


app = Dash(__name__, title='Matemática UFOB')
server = app.server #só serve para subir no render

app.layout = html.Div([
    html.Header(html.H1('Disciplinas de Matemática UFOB-LEM')),
    html.Div([
        html.Nav(
            html.Div([
                html.Div(className='bar'),
                html.Div(className='bar'),
                html.Div(className='bar'),
            ], className= 'burger-menu', id= 'burger-menu', n_clicks=0),
        className='navbar' ),
    ]),
    html.Div(id='saida-menu'),
    html.Div()
])

menu = html.Ul([
            html.Li(html.A('Cálculo 1', href='')),
            html.Li(html.A('Àlgebra', href='')),
            html.Li(html.A('Geometria Analítica', href='')),
        ], id= 'menu')

conteudo = html.Div([
    html.H3('Apresentação'),
    html.P('Esse site foi desenvolvido na Universidade Federal do Oeste da Bahia. ')
])


@app.callback(
    Output('saida-menu', 'children'),
    Input('burger-menu', 'n_clicks')
)
def f(n_clicks):
    if n_clicks % 2 == 1:
        return menu
    else:
        return conteudo








if __name__ == '__main__':
    app.run_server(debug=True)