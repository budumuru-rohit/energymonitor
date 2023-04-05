from django.shortcuts import render,redirect
from base.models import energymonitor
import datetime


# Create your views here.
def home(request):
    return render(request,"app/home.html")

def base(request):
    print('base')
    # i am redirecting it directly to power page temporarily
    # return render(request,"app/power.html")
    return render(request,"app/base.html")
def workshop(request):
    print('workshop')
    return render(request,"app/workshop.html")
# cols = plotly.colors.DEFAULT_PLOTLY_COLORS
def oee(request):
    print('oee')
    table=energymonitor.objects.all()
    y=[float(c.current_r) for c in table]
    print(y)
   
    fig = make_subplots(rows=1, cols=3,subplot_titles=("Current_r", "current_y", "current_b"))
    fig.add_trace(go.Scatter(y=[c.current_r for c in table],x=[c.day for c in table], mode="lines", marker=dict(color='#FF0000'),name='r-phase'), row=1, col=1)
    fig.add_trace(go.Scatter(y=[c.current_y for c in table],x=[c.day for c in table], mode="lines",marker=dict(color='#FFFF00'),name='y-phase'), row=1, col=2)
    fig.add_trace(go.Scatter(y=[c.current_b for c in table],x=[c.day for c in table], mode="lines",marker=dict(color='#0000FF'),name='b-phase'), row=1, col=3)
    fig.update_layout(
                  title_text="Current consumption @ lathe")
    fig.update_xaxes(title_text="Day",showgrid=False)
    fig.update_yaxes(title_text="Ampere",showgrid=False)
    # fig=px.line( 
    #     x=[c.day for c in table],
    #     y=[c.current_r for c in table],row=1,column=1
    # )
    chart=fig.to_html()
    context={'chart':chart,'y':y}
    return render(request,"app/oee.html",context)


def power(request):
    print('power')
    table=energymonitor.objects.all()
    x=[c.day for c in table]
    r=[float(c.current_r) for c in table]
    y=[float(c.current_y) for c in table]
    b=[float(c.current_b) for c in table]
    context={'r':r,'y':y,'b':b,'x':x}
    return render(request,"app/power.html",context)
    
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

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


    
   