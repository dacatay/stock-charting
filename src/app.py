import pandas as pd
import requests

import datetime
from dateutil import parser


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go


#start = datetime.datetime.today() - relativedelta(year=5)
#end = datetime.datetime.today()


### NEWS APP
def update_news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=316d6002c66f43deb1f6363c28cefa8c')
    response = requests.get(url)
    json_string = response.json()
    df = pd.DataFrame(json_string)
    df = df.head()      # might exclude head, since max_rows controls length of news
    return df


# generate news html table
def generate_html_table(max_rows=5):

    df = update_news()
    return html.Div(
        [
            html.Div(
                html.Table(
                    # Header
                    [html.Tr([html.Th()])]
                    +
                    #Body
                    [
                        html.Tr(
                            [
                                html.Td(
                                    html.A(df.iloc[i]['status'], href='https://iextrading.com/developer/docs/#markets', target='_blank')
                                )
                            ]
                        )
                        for i in range(min(len(df), max_rows))
                    ]
                ), style={'height': '400px', 'overflow': 'scroll'}
            )
        ], style={'height': '100%'}
    )


### INITIALIZE DASH INSTANCE
app = dash.Dash(__name__)

# Design layout
app.layout = html.Div([

    html.Div([
        html.H2('Stock App'),
        html.Img(src='/assets/stock-icon.png')
    ], className='banner'),

    html.Div([
        dcc.Input(id='stock-input', value='MSFT', type='text'),
        html.Button(id='submit-button', n_clicks=0, children='Submit')
    ]),

    html.Div([
        html.Div([
            dcc.Graph(id='stock-graph')
        ],  className='six columns'),

        html.Div([
            html.H3('Market news'),
            # call generate function
            generate_html_table()
        ], className='six columns'),

    ], className='row')
])


# include external stylsheets
css_urls = [
    'https://codepen.io/rmarren1/pen/mLqGRg.css',
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]
for url in css_urls:
    app.css.append_css({
        "external_url": url
    })



### Create Callbacks
@app.callback(Output('stock-graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('stock-input', 'value')]
              )
def update_fig(n_clicks, input_value):

    ticker = input_value

    df = pd.read_csv('../data/{ticker}.csv'.format(ticker=ticker), sep=';', index_col=0, header=0)
    df = df.iloc[-720:]

    # plots on the page
    trace_candle = go.Candlestick(x=df.index,
                                  open=df.open,
                                  high=df.high,
                                  low=df.low,
                                  close=df.close,
                                  name='Candle',
                                  showlegend=False)

    data = [trace_candle]

    layout = dict(
        title=input_value,
        autosize=False,
        xaxis=go.layout.XAxis(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )

    return {
        'data': data,
        'layout': layout
    }


if __name__ == '__main__':
    app.run_server(debug=True)
