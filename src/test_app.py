import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Output, Input, State


from iexfinance.stocks import get_historical_data
import datetime
from dateutil.relativedelta import relativedelta

import plotly.graph_objs as go

import pandas as pd
import requests

start = datetime.datetime.today() - relativedelta(year=5)
end = datetime.datetime.today()


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
            dcc.Graph(id='graph_close')
        ],  className='six columns'),

        html.Div([
            html.H3('Market news'),
            # call generate function
            generate_html_table()
        ], className='six columns'),

    ], className='row')
])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


### Create Callbacks
@app.callback(Output('graph_close', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('stock-input', 'value')]
              )
def update_fig(na_clicks, input_value):

    ticker = input_value

    df = pd.read_csv('../data/{ticker}.csv'.format(ticker=ticker), sep=';', index_col=0, header=0)

    # plots on the page
    trace_line = go.Scatter(x=list(df.index),
                            y=list(df.close),
                            name='Line',
                            line=dict(color='#f44242'),
                            showlegend=False)

    trace_candle = go.Candlestick(x=df.index,
                                  open=df.open,
                                  high=df.high,
                                  low=df.low,
                                  close=df.close,
                                  name='Candle',
                                  showlegend=False)

    trace_bar = go.Candlestick(x=df.index,
                               open=df.open,
                               high=df.high,
                               low=df.low,
                               close=df.close,
                               name='Candle',
                               showlegend=False)

    data = [trace_line, trace_candle, trace_bar]

    updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False]}],
                    label='Line',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False]}],
                    label='Candle',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True]}],
                    label='Bar',
                    method='update'
                )

            ]),
            direction='down',
            pad=dict(
                r=10,
                t=10,
            ),
            x=0,
            xanchor='left',
            y=1.05,
            yanchor='top'
        )
    ])

    layout = dict(
        title=input_value,
        updatemenus=updatemenus,
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
