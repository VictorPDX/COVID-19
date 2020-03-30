#!usr/bin/env python

import numpy as np
import requests
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style("whitegrid")


def load(fname="data/data-bxEvA.csv"):
    data = np.genfromtxt(fname, dtype=None, encoding=None, delimiter=',')
    return data

def graph(data):
    # Color palette
    blue, = sns.color_palette("muted", 1)
    
    # header does not count
    days = data.shape[0] - 1

    # Create data
    x = np.arange(days)
    y = data[1:,1]
    
    # Make the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, color=blue, lw=3)
    ax.fill_between(x, 0, y, alpha=.3)
    ax.set(xlim=(0, len(x) - 1), ylim=(0, None), xticks=x)

    print("hi")

def test():
    # create some fictive access data by hour
    xdata = np.arange(25)
    ydata = np.random.randint(10, 20, 25)
    ydata[24] = ydata[0]

    # let us make a simple graph
    fig = plt.figure(figsize=[7,5])
    ax = plt.subplot(111)
    l = ax.fill_between(xdata, ydata)

    # set the basic properties
    ax.set_xlabel('Time of posting (US EST)')
    ax.set_ylabel('Percentage of Frontpaged Submissions')
    ax.set_title('Likelihood of Reaching the Frontpage')

    # set the limits
    ax.set_xlim(0, 24)
    ax.set_ylim(6, 24)

    # set the grid on
    ax.grid('on')

def main():
    test()
    data = load()
    graph(data)
    print(data)



if __name__ == "__main__": 
    print("Executed when invoked directly")
    main()
else: 
    print("Executed when imported")

