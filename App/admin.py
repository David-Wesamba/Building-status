from django.contrib import admin
from .models import Data



class DataAdmin(admin.ModelAdmin):
    list_display = ('name','occupancy', 'floors','wall_thickness','soil_type','predictions')

admin.site.register(Data, DataAdmin)