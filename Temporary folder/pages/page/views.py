from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
# Create your views here.
def index(request, pagenumber):
    pagenumber = '/' + pagenumber
    pg = Page.objects.get(parmanent_links = pagenumber)
    context = {
        'title' : pg.title,
        'content': pg.text_area,
        'last_updated' : pg.published_date,
        'page_list': Page.objects.all(),
        
    }
    return render(request,'page/page.html', context)