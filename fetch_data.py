import pandas as pd
import numpy as np
import time

import pandas_datareader.data as web



def fetch_data(ticker, provider, start, end):

    try:
        print('Fetching {ticker} data...'.format(ticker=ticker))
        df = web.DataReader(ticker, provider, start, end)
        df.to_csv('./data/{ticker}.csv'.format(ticker=ticker), sep=';', index=True, header=True)
        print('Fetching {ticker} data complete.'.format(ticker=ticker))
        time.sleep(3)

    except Exception as e:
        print('main loop', e)


def main():
    tickers = ['AAPL', 'MSFT']
    provider = 'yahoo'
    start = '2017-01-01'
    end = '2017-12-01'

    for ticker in tickers:
        fetch_data(ticker, provider, start, end)


if __name__ == '__main__':
    main()
