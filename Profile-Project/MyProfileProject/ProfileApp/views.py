from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ProfileView(TemplateView):

    template_name='ProfileTemplate.html'
    def View_Me(self):
        return "Inside Profile app"
