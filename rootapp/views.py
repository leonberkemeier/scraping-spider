from http.client import HTTPResponse
from django.shortcuts import render
# from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

import datetime

import threading


def home(request):
    return render (request, "rootapp/scraper.html")


def getdatetime(request):
    now = datetime.datetime.now()
    print ("now is")
    print(now)

    
# def scraper(request):
#     return render (request, "scraper.html")
