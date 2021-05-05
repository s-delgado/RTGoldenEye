import csv

fieldnames = ["timestamp", "feed", "symbol", "bid", "ask"]

with open('data/data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


async def ticker(feed, symbol, bid, ask, timestamp, receipt_timestamp):
    with open('data/data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "timestamp": timestamp,
            "feed": feed,
            "symbol": symbol,
            "bid": bid,
            "ask": ask,
        }
        csv_writer.writerow(info)


async def book(feed, symbol, book, timestamp, receipt):
    with open('data/data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "timestamp": timestamp,
            "feed": feed,
            "symbol": symbol,
            "bid": max(book["bid"]),
            "ask": min(book["ask"]),
        }
        csv_writer.writerow(info)

