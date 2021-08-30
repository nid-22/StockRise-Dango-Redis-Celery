from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceUpdate.settings')

app = Celery('PriceUpdate')
app.conf.enable_utc = False #we are using asia kolkata

app.conf.update(timezone = 'Asia/Kolkata') #A and K shud be capital

app.config_from_object(settings, namespace='CELERY')
#will autodiscover tasks.py from inside the app folders 
app.autodiscover_tasks()
app.conf.beat_schedule={
    # 'every-10-seconds':{
    #     'task':'mainapp.tasks.stockUpdate',
    #     'schedule':10,
    #     'args':(['BHARTIARTL.NS'],)

    # }
}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')