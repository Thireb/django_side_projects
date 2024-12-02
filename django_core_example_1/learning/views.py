from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime

# Create your views here.

def index(request):
    
    return HttpResponse('<h1> hello world </h1>')
    
def time_calc(request,hours):
    
    try:
        hours = int(hours)
    except Exception:
        raise Http404()
    time = datetime.datetime.now() + datetime.timedelta(hours=hours)
    message = "<h1> Your original time {}, added with hours is now {}  </h1>".format(datetime.datetime.now(),time)
    return HttpResponse(message)