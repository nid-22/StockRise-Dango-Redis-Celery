from django.contrib import admin
from .models import PriceLookUpEvent,Company
# Register your models here.

class PriceLookUpEventAdmin(admin.TabularInline):
    model =PriceLookUpEvent
    extra=0

class CompanyAdmin(admin.ModelAdmin):
    inlines=[PriceLookUpEventAdmin]
    class meta:
        model = Company

admin.site.register(Company,CompanyAdmin)
admin.site.register(PriceLookUpEvent)
