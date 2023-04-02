from django.contrib import admin

from .models import energymonitor
class energymonitoradmin(admin.ModelAdmin):
    list_display=['day','month','year','hour','minute','second','microsecond','current_r','current_y','current_b','voltage_r','voltage_y','voltage_b','avg_current','avg_voltage','power']
admin.site.register(energymonitor,energymonitoradmin)

# Register your models here.
