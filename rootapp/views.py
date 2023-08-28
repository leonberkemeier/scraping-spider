from http.client import HTTPResponse
from django.shortcuts import render
# from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from . models import Book
import datetime
from django.db import models
import threading
import pandas as pd
import plotly.express as px
from plotly.offline import plot


def home(request):
    data = Book.objects.all()
    first= data[0]
    return render (request, "rootapp/scraper.html",{'data': data , 'first':first} )


# def getdatetime(request):
#     now = datetime.datetime.now()
#     print ("now is")
#     print(now)

    
# def scraper(request):
#     return render (request, "scraper.html")

def dar(request):

    data = Book.objects.all()
    
    first= data[0]

    crt = Book.objects.all()

    projects_data = [
        {
            'Item': x.name,
            'Price': x.price,
            'Time': x.time,         
        } for x in crt
    ]
    df = pd.DataFrame(crt)
    

    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {'plot_div': gantt_plot}
    
    return render(request, "rootapp/chart.html",{'data': data , 'first':first,'plot_div': gantt_plot})


def chart(request):
    data = data = Book.objects.all()
    return render(request, "rootapp/chunkychart.html",{'data': data,})