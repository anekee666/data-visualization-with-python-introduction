import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('obama.csv', parse_dates=['year_month'])


def plot_aggregation():
    data_mean = data.groupby('year_month').mean()
    data_median = data.groupby('year_month').median()
    data_25 = data.groupby('year_month').quantile(0.25)
    data_75 = data.groupby('year_month').quantile(0.75)
    plt.plot(data_75.index, data_75.approve_percent, 'green')
    plt.plot(data_median.index, data_median.approve_percent, 'red')
    plt.plot(data_25.index, data_25.approve_percent, 'blue')
    plt.plot(data_25.index, data_mean.approve_percent, 'yellow')
    plt.plot(data.year_month, data.approve_percent, 'o', markersize=2,
             alpha=0.3)
    plt.legend(['75th Percentile', 'Median', '25th Percentile', 'Mean'])
    plt.show()


plot_aggregation()
