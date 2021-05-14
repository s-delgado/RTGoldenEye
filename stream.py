from cryptofeed.callback import TradeCallback, BookCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance, Huobi, OKEx, Upbit, FTX, Bybit, Kraken, KuCoin, Bitmex, Bitfinex, BinanceFutures
from cryptofeed.defines import TRADES, L2_BOOK
from save_data import book
import asyncio
import os


symbol = "BTC-USDT"
bitmex_symbol = "BTC-USD"
kwargs = {'max_depth': 20,
          # 'snapshot_interval': 1,
          'channels': [L2_BOOK],
          'callbacks': {L2_BOOK: BookCallback(book)},
          'symbols': [symbol]}

f = FeedHandler()


def delete_files():
    files = ['data/' + x for x in os.listdir('data/') if x[0:4] == 'book']
    for file in files:
        os.remove(file)


def stop():
    loop = asyncio.get_event_loop()
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    # f.add_feed(Binance(**kwargs))
    # f.add_feed(Huobi(**kwargs))
    # f.add_feed(OKEx(**kwargs))
    # # AVOID f.add_feed(Upbit(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    # f.add_feed(FTX(**kwargs))
    # # AVOID f.add_feed(Bybit(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookRedis()}))
    # f.add_feed(Kraken(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    # f.add_feed(KuCoin(**kwargs))
    f.add_feed(Bitmex(symbols=[bitmex_symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    # f.add_feed(Bitfinex(**kwargs))
    # f.add_feed(BinanceFutures(**kwargs))

    f.run(start_loop=False)
    loop.call_later(30, stop)
    print('start')
    loop.run_forever()
    print('end')


if __name__ == '__main__':
    delete_files()
    main()




