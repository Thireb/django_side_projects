from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    one_post = Post.objects.get(id=pk)
    return render(request,'posts.html',{'one_post':one_post})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
        
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used.')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used.')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password does not match.')
            return redirect('/signup')
    else:
        return render(request,'signup.html')