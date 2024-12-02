import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import BlockModel, SpaceModel
# Create your views here.

def logoutView(request):
    auth.logout(request)
    return redirect('/index')

def loginView(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render(request,'login.html')



def register(request):
    #todo
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already registered.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords didn't match.")
            return redirect('register')
            
    else:
        return render(request,'register.html')

def index(request):
    context = {
        'name' : 'Ahmad',
        'age': '22',
        'country': 'Pakistan'
    }
    return render(request,template_name='index.html', context=context)

def counter(request):
    #Methond = GET
    #alfaaz = request.GET['words']
    #tareekh = request.GET['date']
    #Method = POST
    alfaaz = request.POST['words']
    tareekh = request.POST['date']
    total_words = len(alfaaz.split())
    context = {
        'amount' : total_words,
        'date' : tareekh
    }
    return render(request,template_name='counter.html', context=context)
def blockView(request):
    firstBlock = BlockModel()
    firstBlock.text = "I'm the 1st block"
    secondBlock = BlockModel()
    secondBlock.text = "I'm the 2nd block"
    thirdBlock = BlockModel()
    thirdBlock.text = "I'm the 3nd block"
    
    blockList = [firstBlock,secondBlock,thirdBlock]
    return render(request,'block.html',{'blockList':blockList})

def spaceView(request):
    data = SpaceModel.objects.all()
    return render(request,'space.html',{'data':data})