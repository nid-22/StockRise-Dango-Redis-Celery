
from django.urls import path
from .views import *

urlpatterns = [
    
    path('stockupdate', Scrape_view,name='stockUpdate' )
]
