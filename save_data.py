import os
import aiofiles
import csv

depth = 20


def is_file_empty(file_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0


async def book(feed, symbol, book, timestamp, receipt):
    file_name = 'data/book-'+feed+'-'+symbol+'.csv'
    async with aiofiles.open(file_name, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line = [str(timestamp), feed, symbol, str(book['bid']), str(book['ask'])]
        await writer.writerow(line)
