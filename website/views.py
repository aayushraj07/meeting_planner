from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to Meeting Planner!")

def date(requests):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("My name is Aayush")