from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .forms import QuoteForm
from .models import QuoteModel

# Create your views here.

class Register(CreateView):
    model = QuoteModel
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)




@login_required(login_url=reverse_lazy('login'))
def formView(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            try:
                quote.name = request.user
            except Exception:
                pass
            quote.save()
            return HttpResponseRedirect('display/?submitted=True')
    else:
        form = QuoteForm()
        if submitted in request.GET:
            submitted=True
    
    return render(request,'display.html',{'form':form,'submitted':submitted})



class QuoteDetailView(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('login')
    model = QuoteModel
    template_name = "detail_list.html"
    context_object_name = 'quote'
