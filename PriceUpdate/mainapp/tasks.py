from celery import Celery
from celery.app import shared_task

from yahoo_fin.stock_info import *
from threading import Thread
from queue import Queue
from channels.layers import get_channel_layer
import asyncio
import simplejson

@shared_task(bind=True)
def stockUpdate(self,stocks):    
    print(stocks)
    stockData = {}
    threadlist = []
    que = Queue()
    
    # stockData = {}
    # for i in stocks:
    #     stockData.update({i:get_quote_table(i)})
    N_threads = len(stocks)
    for i in range(N_threads):
        thread_ = Thread(target=lambda q,x:q.put({x:simplejson.loads(simplejson.dumps(get_quote_table(x), ignore_nan = True))}),args=(que,stocks[i]))
        threadlist.append(thread_)
        threadlist[i].start()

    for t in threadlist:
        t.join()

    while not que.empty():
        result = que.get()
        stockData.update(result)

     # send data to group
    channel_layer = get_channel_layer()
    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

    #type will be same as the function that recieves this in consumers.py
    loop.run_until_complete(channel_layer.group_send("stock_track", {
        'type': 'send_stock_update',
        'message': stockData,
    }))
            
    return 'done'