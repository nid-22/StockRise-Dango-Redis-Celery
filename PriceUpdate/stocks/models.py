from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
class Company(models.Model):
    Name = models.CharField(max_length=200)
    Ticker = models.CharField(max_length=20)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.Name}" #make sure to return a string
    class Meta:
        ordering=['Name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


SOURCES={
       ('business_insider','Business Insider'),
       ('Echo', 'Echo') 
    }
class PriceLookUpEvent(models.Model):
    Company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=200)
    Ticker = models.CharField(max_length=20, null=True)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    source = models.CharField(max_length=100,choices=SOURCES)

def PriceLookUpEvent_postsave(sender, instance,created, *args, **kwargs):
    if created:
        try:
            obj = Company.objects.get(Ticker__iexact =  instance.Ticker)
            instance.Company = obj
            instance.save()
        except ObjectDoesNotExist:
            print('')
            
post_save.connect(PriceLookUpEvent_postsave,sender=PriceLookUpEvent)