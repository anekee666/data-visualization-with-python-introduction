import pandas as pd
from matplotlib import pyplot as plt


def draw_bar():
    x = range(10)
    plt.bar(x, top10.population / 10 ** 6)
    plt.xticks(x, top10.country, rotation='vertical')
    plt.title('10 Most Populous Countries')
    plt.ylabel('Population in Millions')
    plt.show()


def draw_bar_char_side_by_side():
    plt.subplot(2, 1, 1)
    x = range(10)
    plt.bar(x, top10.population / 10 ** 6)
    plt.xticks([], [])
    plt.title('10 Most Populous Countries')
    plt.legend(['Population in Millions'])
    plt.subplot(2, 1, 2)
    plt.bar(x, top10.gdpPerCapita * top10.population / 10 ** 9)
    plt.xticks(x, top10.country, rotation='vertical')
    plt.legend(['GDP in Billions'])
    plt.show()


def draw_bar_char_both_in_same_char():
    import numpy as np  # We're going to import np for np.arange().
    # np.arange(10) is similar to range(10), and it allows us to shift
    # each value in it by the bar width as you can see below.
    x = np.arange(10)

    # We need to create subplots in order to overlay two bar plots
    # with proper axes on the left hand side and the right hand side.
    fig, ax1 = plt.subplots()

    width = 0.3  # This is the width of each bar in the bar plot.
    plt.xticks(x, top10.country, rotation='vertical')
    population = ax1.bar(x, top10.population / 10 ** 6, width)
    plt.ylabel('Population')

    # ax1.twinx() gives us the same x-axis with the y-axis on the right.
    ax2 = ax1.twinx()
    gdp = ax2.bar(x + width, top10.gdpPerCapita * top10.population / 10 ** 9,
                  width, color='orange')
    plt.ylabel('GDP')
    plt.legend([population, gdp],
               ['Population in Millions', 'GDP in Billions'])
    plt.show()


data = pd.read_csv("countries.csv")
data_2007 = data[data.year == 2007]
top10 = data_2007.sort_values('population', ascending=False).head(10)
# draw_bar()
# draw_bar_char_side_by_side()
draw_bar_char_both_in_same_char()
