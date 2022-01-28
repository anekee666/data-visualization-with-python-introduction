import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def sample_scatter(x, y, size=5):
    plt.scatter(x, y, size)
    plt.title('GDP Per Capita and Life Expectancy in 2007')
    plt.xlabel('GDP Per Capita ($)')
    plt.ylabel('Life Expectancy')
    plt.show()
    print(x.corr(y))


def create_scatter_charts(data):
    years_sorted = sorted(set(data.year))

    for given_year in years_sorted:
        data_year = data[data.year == given_year]
        plt.scatter(data_year.gdpPerCapita, data_year.lifeExpectancy, 5)
        plt.title(given_year)
        plt.xlim(0, 60000)
        plt.ylim(25, 85)
        plt.xlabel('GDP Per Capita')
        plt.ylabel('Life Expectancy')
        #     plt.show()
        plt.savefig(str(given_year), dpi=200)  # dpi = dots per inch
        plt.clf()  # We need this line to clear the current plot.


data = pd.read_csv('countries.csv')
data_2007 = data[data.year == 2007]

sample_scatter(data_2007.gdpPerCapita, data_2007.lifeExpectancy)
# (np.log10(data_2007.gdpPerCapita),data_2007.lifeExpectancy,50)
#create_scatter_cahrts(data)