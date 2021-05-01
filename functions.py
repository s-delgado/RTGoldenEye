import pandas as pd
import numpy as np


def generate_volumebars(df, frequency=10):
    trades = df[['E', 'p', 'q']].values
    times = trades[:, 0]
    prices = trades[:, 1]
    volumes = trades[:, 2]
    ans = np.zeros(shape=(len(prices), 6))
    candle_counter = 0
    vol = 0
    lasti = 0
    for i in range(len(prices)):
        vol += volumes[i]
        if vol >= frequency:
            ans[candle_counter][0] = times[i]                          # time
            ans[candle_counter][1] = prices[lasti]                     # open
            ans[candle_counter][2] = np.max(prices[lasti:i+1])         # high
            ans[candle_counter][3] = np.min(prices[lasti:i+1])         # low
            ans[candle_counter][4] = prices[i]                         # close
            ans[candle_counter][5] = np.sum(volumes[lasti:i+1])        # volume
            candle_counter += 1
            lasti = i+1
            vol = 0
    bars = pd.DataFrame(ans[:candle_counter],
                        columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    bars.set_index(pd.to_datetime(bars.timestamp, unit='us'), inplace=True)
    bars.drop(columns=['timestamp'], inplace=True)
    return bars
