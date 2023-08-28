from turtle import home
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    # path('scraper', views.scraper, name="scraper"),
    path('dar', views.dar, name="dar"),
    path('chart', views.chart, name="chart"),

    
    



]