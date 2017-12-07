import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


def plot_data(ticker):

    date, openp, highp, lowp, closep, adjp, volume = np.loadtxt('./data/{ticker}.csv'.format(ticker=ticker),
                                                                    delimiter=';',
                                                                    skiprows=1,
                                                                    unpack=True,
                                                                    converters={1: mdates.strpdate2num('%Y-%m-%d')})

    fig = plt.figure()
    ax1 = plt.subplot(1, 1, 1)
    ax1.plot(date, openp)

    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.show()



ticker = 'AAPL'
plot_data(ticker)