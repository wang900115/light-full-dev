from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login 
##註冊
def register(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password :
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
            else:
                User.objects.create_user(username=username,password=password)
                messages.success(request,'Account created successfully')
                return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
    return render(request,'user/register.html')
    
##登入
def login_view(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user :
            login(request,user)
            return redirect('list-event')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'user/login.html')




