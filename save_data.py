import csv
import os
import aiofiles

depth = 20


def is_file_empty(file_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0


async def book(feed, symbol, book, timestamp, receipt):
    file_name = 'data/book-'+feed+'-'+symbol+'.csv'
    async with aiofiles.open(file_name, 'a') as csv_file:
        data = {
            "timestamp": timestamp,
            "feed": feed,
            "symbol": symbol,
            "bid": max(book["bid"]),
            "ask": min(book["ask"]),
            "bookSize": len(book['ask']),
            "bidQuantityAll": sum(book["bid"].values()),
            "askQuantityAll": sum(book["ask"].values()),
            "bidQuantity": sum(book["bid"].values()[-depth:]),
            "askQuantity": sum(book["ask"].values()[0:depth]),
        }
        line = []

        for c in data.keys():
            line.append(str(data.get(c, '')))

        line = ','.join(line) + '\n'

        await csv_file.write(line)
