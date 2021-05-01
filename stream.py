from binance.client import Client
from keys import keys
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from save_data import process_message, process_message2
import time

client = Client(keys['binance']['apiKey'], keys['binance']['secret'])
bm = BinanceSocketManager(client)
bm2 = BinanceSocketManager(client)

conn_key = bm.start_aggtrade_socket('BTCUSDT', process_message)
conn_key2 = bm2.start_aggtrade_futures_socket('BTCUSDT', process_message2)

bm.start()
bm2.start()

time.sleep(120)
print("end")
bm.close()
bm2.close()
reactor.stop()
