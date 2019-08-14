import time
import datetime

import yfinance as yf


def fetch_yfinance_data(ticker, start, end):
    try:
        print('Fetching {ticker} data...'.format(ticker=ticker))
        data = yf.Ticker(ticker)

        df = data.history(start=start, end=end)

        df.to_csv('../data/{ticker}.csv'.format(ticker=ticker), sep=';', index=True, header=True)
        print('Fetching {ticker} data complete.'.format(ticker=ticker))
        time.sleep(2)

    except Exception as e:
        print('Fetch ticker data: ', e)


def main():
    tickers = ['MSF.DE', 'AMZ.DE', 'CMC.DE', 'PFE.DE', 'CIS.DE', 'HDI.DE', 'MDO.DE', 'AEC1.DE', 'WDP.DE', 'JNJ.DE',
               '3V64.DE']
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.today()

    for ticker in tickers:
        fetch_yfinance_data(ticker, start, end)


if __name__ == '__main__':
    main()
