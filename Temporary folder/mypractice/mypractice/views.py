from django.http import HttpResponse

def firstWebView(request):
    return HttpResponse('Im the firtst view man.')