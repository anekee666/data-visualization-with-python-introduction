import pandas as pd
from matplotlib import pyplot as plt


def hist(title="", ylable1="",ylable2="", data1=[], data2=[]):
    plt.subplot(2, 1, 1)  # subplot(211)
    plt.title(title)
    plt.hist(data1, 20, range=(0, 50000), edgecolor='black')
    plt.ylabel(ylable1)
    plt.subplot(2, 1, 2)
    plt.hist(data2, 20, range=(0, 50000), edgecolor='black')
    plt.ylabel(ylable2)
    plt.show()


data = pd.read_csv("countries.csv")
print(set(data["continent"]))

data_2007 = data[data.year == 2007]
asia_2007 = data_2007[data_2007.continent == 'Asia']
europe_2007 = data_2007[data_2007.continent == 'Europe']

hist('Distribution of GDP Per Capita', 'Asia', 'Europe', asia_2007.gdpPerCapita, europe_2007.gdpPerCapita)
# len(set(asia_2007["country"]))
# len(set(europe_2007["country"]))
# print('Mean GDP Per Capita in Asia:')
# print(asia_2007.gdpPerCapita.mean())
# print('Mean GDP Per Capita in Europe:')
# print(europe_2007.gdpPerCapita.mean())
# print('Median GDP Per Capita in Asia:')
# print(asia_2007.gdpPerCapita.median())
# print('Median GDP Per Capita in Europe:')
# print(europe_2007.gdpPerCapita.median())
