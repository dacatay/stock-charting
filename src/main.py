import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime

# data



# app layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Charting App'),
    html.Div(children='''
        A web application for Python
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')

])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')])
def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    provider = 'yahoo'
    df = web.DataReader(input_data, provider, start, end)

    return dcc.Graph(id='example-graph',
                     figure={
                         'data': [
                             {'x': df.index,
                              'y': df.Close,
                              'type': 'line',
                              'name': input_data},
                         ],
                         'layout': {
                             'title': 'Closing price for {} shares'.format(input_data)
                         }
                     }),


if __name__ == '__main__':
    app.run_server(debug=True)
