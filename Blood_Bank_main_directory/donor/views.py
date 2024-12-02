from django.db.models import fields
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Donor
# Create your views here.



class HomeView(TemplateView):
    template_name = "home.html"



class DonorCreateView(CreateView):
    model = Donor
    template_name = "add_donor.html"
    fields = "__all__"
    success_url = "/home"



class DonorListView(ListView):
    model = Donor
    template_name = "list_donor.html"
    context_object_name = 'donors'




class DonorDetailView(DetailView):
    model = Donor
    template_name = "detail_donor.html"
    context_object_name = 'donor'
