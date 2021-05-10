import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from functions import generate_volumebars
from fees import taker
import os

colors = ['b', 'g', 'r', 'c', 'm', 'k', 'y', 'plum', 'olive']
fieldnames = ["timestamp", "feed", "symbol", "bid", "ask",
              "bookSize", "bidQuantityAll", "askQuantityAll", "bidQuantity", "askQuantity"]


def animate(j):
    files = ['data/' + x for x in os.listdir('data/') if x[0:4] == 'book']
    plt.cla()
    for i, file in enumerate(files):
        df = pd.read_csv(file, names=fieldnames)
        feed = file.split('-')[1]
        fee = taker[feed]

        y = df['bid'] * (1 - fee)
        y2 = df['ask'] * (1 + fee)
        x = df['timestamp']

        plt.plot(x, y, label='bid_' + feed, color=colors[i])
        plt.plot(x, y2, label='ask_' + feed, color=colors[i])

    plt.legend(loc='upper left')
    plt.tight_layout()
# animate(0)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
