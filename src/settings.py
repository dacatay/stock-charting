import datetime

# COLOR SCHEME AND STYLE
colors = {'background': '#262626',
          'font': 'w',
          'axis': 'w',
          'rsi': '00ffcc'}


# MACRO VARIABLES
tickers = ['MSF.DE', 'AMZ.DE', 'CMC.DE', 'PFE.DE', 'CIS.DE', 'HDI.DE', 'MDO.DE',
           'AEC1.DE', 'WDP.DE', 'JNJ.DE', '3V64.DE', 'BAS.DE', 'MMM.DE', 'UWS.F',
           'WCN', 'RSG', 'BAC', 'NVD.DE', 'DBK.DE', 'KO', 'QCOM', 'BAC.DE', 'HC5.F',
           'KMB', 'MET', 'EA', 'ZNGA', 'GOOG', 'PAYC', 'AAPL', 'FB', 'TSLA', 'NFLX',
           'ATVI', 'BYND', 'PM', 'IIPR', 'BABA', 'DAI.DE']

indices = ['^NDX', '^GDAXI', '^MDAXI', '^GSPC', '^HSI']

etfs = ['C051.F', 'E903.DE', 'EXSG.DE', ]

exrs = ['EURUSD=X']

cryptos = []

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.today()
