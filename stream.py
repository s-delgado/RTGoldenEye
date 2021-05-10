from cryptofeed.callback import TradeCallback, BookCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance, Huobi, OKEx, Upbit, FTX, Bybit, Kraken, KuCoin, Bitmex, Bitfinex
from cryptofeed.defines import TRADES, L2_BOOK
# from cryptofeed.backends.redis import BookRedis
from save_data import book
import asyncio
import redis
import os

# Delete existing data in redis
r = redis.StrictRedis(host='localhost')
for key in r.scan_iter():
    r.delete(key)

symbol = "ETH-USDT"
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
    f.add_feed(Binance(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(Huobi(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(OKEx(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    # AVOID f.add_feed(Upbit(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(FTX(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    # AVOID f.add_feed(Bybit(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookRedis()}))
    f.add_feed(Kraken(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(KuCoin(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(Bitmex(symbols=['ETH-USD'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(Bitfinex(symbols=[symbol], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))

    f.run(start_loop=False)
    loop.call_later(30, stop)
    print('start')
    loop.run_forever()
    print('end')


if __name__ == '__main__':
    delete_files()
    main()




