import time
from alpha_vantage.timeseries import TimeSeries
from iexfinance.stocks import get_historical_data

import datetime
from dateutil.relativedelta import relativedelta

ALPHA_VANTAGE_API_KEY = '.'

NEWSAPI_API_KEY = '.'


start = datetime.datetime.today() - relativedelta(year=5)
end = datetime.datetime.today()

def fetch_ticker_data(ticker, interval):

    try:
        if interval == 'intraday':
            interval = '1min'
            ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
            print('Fetching {ticker} data...'.format(ticker=ticker))
            df, meta_data = ts.get_intraday(symbol=ticker, interval=interval, outputsize='full')

            df.columns = ['open', 'high', 'low', 'close', 'volume']
            df.to_csv('../data/{ticker}_intraday.csv'.format(ticker=ticker), sep=';', index=True, header=True)
            print('Fetching {ticker} data complete.'.format(ticker=ticker))
            time.sleep(2)

        elif interval == 'daily':
            ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
            print('Fetching {ticker} data...'.format(ticker=ticker))
            df, meta_data = ts.get_daily(symbol=ticker, outputsize='full')

            df.columns = ['open', 'high', 'low', 'close', 'volume']
            df.to_csv('../data/{ticker}.csv'.format(ticker=ticker), sep=';', index=True, header=True)
            print('Fetching {ticker} data complete.'.format(ticker=ticker))
            time.sleep(2)

        elif interval == 'daily_adj':
            ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
            print('Fetching {ticker} data...'.format(ticker=ticker))
            df, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')

            df.columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
            df.to_csv('../data/{ticker}_adj.csv'.format(ticker=ticker), sep=';', index=True, header=True)
            print('Fetching {ticker} data complete.'.format(ticker=ticker))
            time.sleep(2)

    except Exception as e:
        print('Fetch ticker data: ', e)


def main():
    tickers = ['AAPL', 'MSFT', 'AMZN']

    # Intervals are: daily, daily_adj, intraday
    intervals = ['daily']
    for interval in intervals:
        for ticker in tickers:
            fetch_ticker_data(ticker, interval=interval)


if __name__ == '__main__':
    main()
