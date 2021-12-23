import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# kill -9 $(ps -A | grep python | awk '{print $1}')

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('Entascope'),
    html.Div([
        html.P("Color:")

    ]),
    
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Gold', 'MediumTurquoise', 'LightGreen']
        ],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], marker_color=color))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)