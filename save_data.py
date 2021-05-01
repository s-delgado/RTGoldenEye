import csv

fieldnames = ["E", "s", "a", "p", "q", "f", "l", "T", "m"]

with open('data/data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

with open('data/data2.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


def process_message(msg):
    with open('data/data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "E": msg["E"],
            "s": msg["s"],
            "a": msg["a"],
            "p": msg["p"],
            "q": msg["q"],
            "f": msg["f"],
            "l": msg["l"],
            "T": msg["T"],
            "m": msg["m"]
        }
        csv_writer.writerow(info)


def process_message2(msg):
    msg = msg['data']
    with open('data/data2.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "E": msg["E"],
            "s": msg["s"],
            "a": msg["a"],
            "p": msg["p"],
            "q": msg["q"],
            "f": msg["f"],
            "l": msg["l"],
            "T": msg["T"],
            "m": msg["m"]
        }
        csv_writer.writerow(info)


