from django.shortcuts import render,redirect
from base.models import energymonitor
import datetime

def daily_current(request):
    latest_date=energymonitor.objects.latest('day')
    latest_record_r = energymonitor.objects.latest('current_r')
    data = {
    'field1': latest_date,
    'field2': latest_record_r,
    }
    context = {'latest_record_data': data}
    return render(request, "app/power.html", context)

# Create your views here.
def base(request):
    print('base')
    # i am redirecting it directly to power page temporarily
    return render(request,"app/power.html")
    return render(request,"app/base.html")
def workshop(request):
    print('workshop')
    return render(request,"app/workshop.html")

def oee(request):
    print('oee')
    return render(request,"app/oee.html")
def power(request):
    print('power')
    return render(request,"app/power.html")
    
def data_view(request):
    current_time = datetime.datetime.now()
    year=current_time.year
    month=current_time.month
    day=current_time.day
    hour=current_time.hour
    minute=current_time.minute
    second=current_time.second
    microsecond=current_time.microsecond
    if request.method=="GET":
        print('request')
        print(request)
        curr_r=float(request.GET.get('current_r'))
        curr_y=float(request.GET.get('current_y'))
        curr_b=float(request.GET.get('current_b'))
        volt_r=float(request.GET.get('voltage_r'))
        volt_y=float(request.GET.get('voltage_y'))
        volt_b=float(request.GET.get('voltage_b'))
        print('curr_r')
        print(curr_r,curr_b,curr_y)
        print('typeof')
        print(type(curr_b),type(volt_b))
        if curr_r!=None and curr_y!=None and curr_b!=None:
            table=energymonitor()
            table.day=day
            table.month=month
            table.year=year
            table.hour=hour
            table.minute=minute
            table.second=second
            table.microsecond=microsecond
            table.current_r=curr_r
            table.current_y=curr_y
            table.current_b=curr_b
            table.voltage_r=volt_r
            table.voltage_y=volt_y
            table.voltage_b=volt_b
            table.avg_current=(curr_r+curr_b+curr_y)/3
            table.avg_voltage=(volt_r+volt_b+volt_y)/3
            avg_curr=(curr_r+curr_b+curr_y)/3
            avg_volt=(volt_r+volt_b+volt_y)/3
            table.power=(avg_curr)*(avg_volt)
            table.save()
            print('sucessc')
    return render(request,'app/data.html',{"curr":curr_r})
   