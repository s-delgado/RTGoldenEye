from cryptofeed.callback import TickerCallback, TradeCallback, BookCallback, FundingCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase, Binance
from cryptofeed.defines import TRADES, TICKER, L3_BOOK, BID, ASK, L2_BOOK


async def ticker(feed, symbol, bid, ask, timestamp, receipt_timestamp):
    print(f'Timestamp: {timestamp} Feed: {feed} Pair: {symbol} Bid: {bid} Ask: {ask}')


async def book(feed, symbol, book, timestamp, receipt_timestamp):
    print(f'Timestamp: {timestamp} Cryptofeed Receipt: {receipt_timestamp} Feed: {feed} Symbol: {symbol} Book Bid Size is {len(book[BID])} Ask Size is {len(book[ASK])}')


async def trade(feed, symbol, order_id, timestamp, side, amount, price, receipt_timestamp):
    print(f"Timestamp: {timestamp} Feed: {feed} Pair: {symbol} ID: {order_id} Side: {side} Amount: {amount} Price: {price}")


def main():
    f = FeedHandler()
    f.add_feed(Binance(symbols=['BTC-USDT'],
                        channels=[L2_BOOK],
                        callbacks={TICKER: TickerCallback(ticker),
                                   TRADES: TradeCallback(trade),
                                   L3_BOOK: BookCallback(book)}))
    loop = asyncio.get_running_loop()

    f.run()
    loop.stop()


if __name__ == '__main__':
    main()