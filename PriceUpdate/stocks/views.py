from django.shortcuts import render
from .scraper import *
from .tasks import perform_scrape
from django.shortcuts import render,HttpResponse
# Create your views here.
def Scrape_view(request):
    perform_scrape.delay()
    return HttpResponse('Done')
