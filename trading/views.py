from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import yfinance as yf

def index(request):
    data = yf.download("BTC-USD AMZN", period="1mo", group_by="tickers")
    context = {
        'data': data,
    }
    return render(request, 'trading/index.html', context)

def start(request):
    return redirect('index')