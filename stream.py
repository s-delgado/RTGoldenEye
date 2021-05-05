from cryptofeed.callback import TickerCallback, TradeCallback, BookCallback, FundingCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance, Huobi, OKEx, Upbit, FTX, Bybit
from cryptofeed.defines import TRADES, TICKER, L3_BOOK, BID, ASK, L2_BOOK
from save_data import book
import asyncio


f = FeedHandler()


def stop():
    loop = asyncio.get_event_loop()
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    f.add_feed(Binance(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(Huobi(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(OKEx(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(Upbit(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(FTX(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
    f.add_feed(Bybit(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))

    print('start')
    f.run(start_loop=False)
    loop.call_later(60, stop)
    loop.run_forever()
    print('end')



if __name__ == '__main__':
    main()




