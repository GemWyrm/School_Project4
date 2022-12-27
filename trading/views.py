from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import yfinance as yf
import finplot as fplt
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import matplotlib.cbook as cbook

def index(request):
    data = yf.download("BTC-USD", period="1mo", group_by="tickers")
    # This is how to do it in the python shell. How to save and recall this info...
    # data2 = yf.download("AMZN", period="1mo")
    fplt.candlestick_ochl(data1[['Open', 'Close', 'High', 'Low']])
    # fplt.candlestick_ochl(data2[['Open', 'Close', 'High', 'Low']])
    fplt.save('graph.png', 'BASE_DIR/graph/')
    context = {
        'data': data,
    }
    return render(request, 'trading/index.html', context)

def start(request):
    return redirect('index')