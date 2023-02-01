from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout



def Register(request):
    form = RegisterForm()
    if request.method == 'POST':
        print('post got ')
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form valid')
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            return redirect('login')
        else:
            print('post returned')
            form = RegisterForm()
    
    return render(request,'register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            print('user found')
            login(request,user)
            return redirect('/')
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


















