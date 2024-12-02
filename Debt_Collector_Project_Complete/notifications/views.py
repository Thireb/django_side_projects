from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #new

from django.urls import reverse_lazy

from .models import Notif
# Create your views here
class HomeView(TemplateView):
    template_name = "home.html"


class NotifListView(ListView):
    model = Notif
    template_name = "notifList.html"
    context_object_name = 'users'

class NotifUpdateView(UpdateView):
    model = Notif
    template_name = "notifUpdate.html"
    fields = ['name', 'debtAmount', 'debtDate']
    success_url = reverse_lazy('Users_list')
    context_object_name = 'users'


class NotifCreateView(CreateView):
    model = Notif
    template_name = "notifCreate.html"
    fields = '__all__'
    success_url = reverse_lazy('Users_list')
    

class NotifDeleteView(DeleteView):
    model = Notif
    template_name = "notifDelete.html"
    success_url = reverse_lazy('Users_list')
    
