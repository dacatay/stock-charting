import time
import pandas as pd
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta


def fetch_yahoo_data(ticker, provider, start, end):

    try:
        if provider == 'yahoo':
            print('Fetching {ticker} data...'.format(ticker=ticker))
            df = web.DataReader(ticker, provider, start, end)

            df.to_csv('../data/{ticker}.csv'.format(ticker=ticker), sep=';', index=True, header=True)
            print('Fetching {ticker} data complete.'.format(ticker=ticker))
            time.sleep(2)

    except Exception as e:
        print('Fetch ticker data: ', e)


def main():
    tickers = ['MSF.DE', 'AMZ.DE', 'CMC.DE', 'PFE.DE', 'CIS.DE', 'HDI.DE', 'MDO.DE', 'AEC1.DE', 'WDP.DE', 'JNJ.DE', '3V64.DE']
    provider = 'yahoo'
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime.today()

    for ticker in tickers:
        fetch_yahoo_data(ticker, provider, start, end)


if __name__ == '__main__':
    main()
