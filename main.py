import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from functions import generate_volumebars

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('data/data.csv')
    feeds = data.feed.unique()
    plt.cla()
    for f in feeds:
        y = data[data.feed == f]['bid']
        x = data[data.feed == f]['timestamp']

        plt.plot(x, y, label='bid_' + f)

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()


# {
#     "e": "aggTrade",  // Event type
# "E": 123456789,   // Event time
# "s": "BNBBTC",    // Symbol
# "a": 12345,       // Aggregate trade ID
# "p": "0.001",     // Price
# "q": "100",       // Quantity
# "f": 100,         // First trade ID
# "l": 105,         // Last trade ID
# "T": 123456785,   // Trade time
# "m": true,        // Is the buyer the market maker?
# "M": true         // Ignore
# }



