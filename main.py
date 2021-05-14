import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sortedcontainers import SortedDict as sd
from decimal import Decimal
# from functions import generate_volumebars
from fees import taker
from arctic import Arctic

colors = ['b', 'g', 'r', 'c', 'm', 'k', 'y', 'plum', 'olive']



def read_book(feed, symbol):
    store = Arctic('mongodb://127.0.0.1:27017')
    library = store[feed]
    it = library.iterator('l2_book-' + symbol)
    book = {'bid': sd(), 'ask': sd()}
    data = {'timestamps': [],
            'bestBid': [],
            'bestAsk': [],
            'bidVolume': [],
            'askVolume': [],
            'bestBidVolume': [],
            'bestAskVolume': [],
            'lastAskLevel': [],
            'lastAskVolume': []}
    for chunk in it:
        chunk['delta'] = chunk.delta.map({'False': False, 'True': True})
        for row in chunk.iterrows():
            timestamp = row[0]
            receipt_timestamp, delta, side, price, size = row[1].values
            delta = bool(delta)
            if size == 0:
                del book[side][price]
            else:
                book[side][price] = size

            if delta and len(book['ask']) == 20 and len(book['bid']) == 20:
                best_bid, best_ask = book['bid'].keys()[-1], book['ask'].keys()[0]
                data['timestamps'].append(timestamp)
                data['bestBid'].append(best_bid)
                data['bestAsk'].append(best_ask)
                data['bidVolume'].append(sum(book['bid'].values()[-15:]))
                data['askVolume'].append(sum(book['ask'].values()[0:15]))
                data['bestBidVolume'].append(book['bid'].values()[-1])
                data['bestAskVolume'].append(book['ask'].values()[0])
                data['lastAskLevel'].append(book['ask'].keys()[-1])
                data['lastAskVolume'].append(book['ask'].values()[-1])
    return pd.DataFrame(data)


feed = 'BITMEX'
data = read_book(feed, 'BTC-USD')


def plot(data):
    # plt.cla()
    y = data['bestBid']
    y2 = data['bestAsk'] #* (1 + fee)
    x = data['timestamps']

    fig, ax = plt.subplots(2, 1, sharex=True)
    ax[0].plot(x, y, label='bid_' + feed, color=colors[0])
    ax[0].plot(x, y2, label='ask_' + feed, color=colors[0])

    ax[1].plot(x, data['bidVolume'], label='bidVolume')
    ax[1].plot(x, data['askVolume'], label='askVolume')

    # ax[1].plot(x, data['bestAskVolume'], label='bestAskVolume')
    # ax[1].plot(x, data['bestBidVolume'], label='bestBidVolume')

    plt.legend(loc='upper left')
    plt.tight_layout()
    # plt.show()

plot(data)

# ani = FuncAnimation(plt.gcf(), animate, interval=1000)

