from django.db.models import fields
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Patient
from django.urls import reverse_lazy
# Create your views here.

class PatientListView(ListView):
    model = Patient
    template_name = "patient_list.html"
    context_object_name = 'patient_list'


class PatientDetailView(DetailView):
    model = Patient
    template_name = "patient_detail.html"
    context_object_name = 'patient_detail'


class PatientUpdateView(UpdateView):
    model = Patient
    template_name = "patient_edit.html"
    fields = '__all__'


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "patient_delete.html"
    success_url = reverse_lazy('patient_list')
    
class PatientCreateView(CreateView):
    model = Patient
    template_name = "patient_new.html"
    fields = '__all__'
