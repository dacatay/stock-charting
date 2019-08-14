import time
import quandl
import datetime


QUANDL_API_KEY = ''
quandl.ApiConfig.api_key = QUANDL_API_KEY


# FREE DATA FROM QUANDL HAS BE DECOMMISSIONED
def fetch_quandl_data(ticker, start, end):
    try:
        print('Fetching {ticker} data...'.format(ticker=ticker))
        df = quandl.get_table('WIKI/PRICES', ticker=[ticker],
                              # qopts = { 'columns': ['date', 'open', 'high', 'low', 'close', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'volume'] },
                              date={'gte': start, 'lte': end},
                              paginate=True)

        df.index = df['date']
        df = df.drop(columns=['ticker', 'date'])

        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Ex Dividend', 'Split Ratio', 'Adjusted Open',
                      'Adjusted High', 'Adjusted Low', 'Adjusted Close', 'Adjusted Volume']

        df.to_csv('../data/{ticker}.csv'.format(ticker=ticker), sep=';', index=True, header=True)
        print('Fetching {ticker} data complete.'.format(ticker=ticker))
        time.sleep(2)

    except Exception as e:
        print('Fetch ticker data: ', e)


def main():
    tickers = ['MSFT', 'AMZN', 'JPM', 'PFE', 'CSCO', 'HDI', 'MCD', 'AEC1', 'WDP', 'JNJ', '3V64']
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime.today()

    for ticker in tickers:
        fetch_quandl_data(ticker, start, end)


if __name__ == '__main__':
    main()
