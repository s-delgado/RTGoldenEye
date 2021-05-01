import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functions import generate_volumebars

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('data/data.csv')
    data = generate_volumebars(data, frequency=1).reset_index()
    data2 = pd.read_csv('data/data2.csv')
    data2 = generate_volumebars(data2, frequency=1).reset_index()

    y1 = data['close'][-50:]  # price
    # x1 = data['timestamp']
    x1 = [x for x in range(50)][-len(y1):]

    y2 = data2['close'][-50:]   # price
    # x2 = data2['timestamp']
    x2 = [x for x in range(50)][-len(y2):]

    plt.cla()
    plt.plot(x1, y1, label='spot')
    plt.plot(x2, y2, label='futures')
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



