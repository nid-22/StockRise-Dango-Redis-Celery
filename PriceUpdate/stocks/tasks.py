from celery import shared_task
from .scraper import StockTickerScraper,SERVICES
from .models import PriceLookUpEvent

#if you dont use the shared task decorator, you cant see it in the celery beat admin
@shared_task()
def perform_scrape(service='business_insider', ticker='AAPL'):
    client = StockTickerScraper(service=service)
    name,price = client.scrape(ticker=ticker)
    P = PriceLookUpEvent.objects.create(Name = name,Price =price,Ticker=ticker, source  = service)
    print(P.Price)

#celery commands
#celery -A PriceUpdate worker....runs the worker process
#celery -A PriceUpdate worker --beat...runs the beat process