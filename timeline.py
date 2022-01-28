import pandas as pd
from matplotlib import pyplot as plt


def line_chart(year1, year2, data1, data2):
    plt.plot(year1, data1)
    plt.plot(year2, data2)
    plt.legend(['United States', 'China'])
    plt.xlabel('year')
    plt.ylabel('GDP per capita')
    plt.show()


data = pd.read_csv('countries.csv')
us = data[data.country == 'United States']
china = data[data.country == 'China']

us_growth = us.gdpPerCapita / us.gdpPerCapita.iloc[0] * 100
china_growth = china.gdpPerCapita / china.gdpPerCapita.iloc[0] * 100

#line_chart(us.year, china.year, us.gdpPerCapita, china.gdpPerCapita)
line_chart(us.year, china.year, us_growth, china_growth)