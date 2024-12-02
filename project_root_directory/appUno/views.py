from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import PagesModel
from .forms import contact
from django.core.mail import get_connection, send_mail
# Create your views here.

def index(request,pagename):
    
    page = PagesModel.objects.get(name=pagename)
    context = {
        'Name' : page.name,
        'Body' : page.body
    }
    return render(request,'home.html',context)

def contactFormView(request):
    submitted = False
    if request.method == 'POST':
        form = contact(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cleaned_form['name'],
                cleaned_form['permalink'],
                cleaned_form.get('email','noreply@email.com'),
                ['siteowner@email.com'],
                connection=con
            )
            return HttpResponseRedirect('contact?submitted=True')
    else:    
        form = contact()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'form.html',{'form':form, 'submitted':submitted})
    
def displayForm(request):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    context = {
        'first' : firstName,
        'last' : lastName,
    }
    return render (request,'display.html',context)