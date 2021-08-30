
from django.urls import path
from .views import *

urlpatterns = [
    
    path('stockPicker', stockPicker,name='stockPicker' ),
    path('stockTracker', stockTracker,name='stockTracker' )
   
]
