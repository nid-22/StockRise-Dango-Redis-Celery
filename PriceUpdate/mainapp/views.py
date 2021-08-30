from django.shortcuts import render
from yahoo_fin.stock_info import *
from threading import Thread
from queue import Queue

def stockPicker(request):
    tickers = tickers_nifty50()
    return render(request,'mainapp/stockPicker.html',{'tickers':tickers})
import time
def stockTracker(request):
    
    stocks = request.GET.getlist('stockpicker')
    print(stocks)
    stockData = {}
    threadlist = []
    que = Queue()
    start = time.time()
    # stockData = {}
    # for i in stocks:
    #     stockData.update({i:get_quote_table(i)})
    N_threads = len(stocks)
    for i in range(N_threads):
        thread_ = Thread(target=lambda q,x:q.put({x:get_quote_table(x)}),args=(que,stocks[i]))
        threadlist.append(thread_)
        threadlist[i].start()

    for t in threadlist:
        t.join()

    while not que.empty():
        result = que.get()
        stockData.update(result)
    end = time.time()
    delta = end-start
    print(delta)
    return render(request,'mainapp/stockTracker.html',{'stockData':stockData,'room_name':'track'})