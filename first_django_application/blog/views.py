from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse


def home(request):
    #handle traffic of the blog.
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #what user sees when sent to this route.
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #what user sees when sent to this route.
