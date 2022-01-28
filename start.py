from matplotlib import pyplot as plt
import pandas as pd


def plot_demo(title="", x_label="", y_label="", x_list=[], y_list=[]):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_list, y_list, '-o')
    plt.show()


def plot_2_chart(x_list1=[], y_list1=[], x_list2=[], y_list2=[], legend=[]):
    plt.plot(x_list1, y_list1)
    plt.plot(x_list2, y_list2)
    plt.legend(legend)  # plt.legend() takes a list as an argument.
    # plt.savefig('exported_image')
    plt.show()


def create_df():
    data = {'year': [2008, 2012, 2016],
            'attendees': [112, 321, 729],
            'average age': [24, 43, 31]}
    return pd.DataFrame(data)


df = create_df()
plot_demo("Mul 3", "x_num", "y_num", df['year'], df['attendees'])
# plot_2_chart(df['year'], df['attendees'], df['year'], df['average age'], ['attendees', 'average age'])
# print(df.head())

