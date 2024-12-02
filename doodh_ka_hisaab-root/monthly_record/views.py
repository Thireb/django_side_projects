from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RecordForm
# Create your views here.
def homeView(request):
    
    submitted = False
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/record?submitted=True')
    else:
        form = RecordForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'monthly_record/record_save.html',{'form': form, 'submitted': submitted})