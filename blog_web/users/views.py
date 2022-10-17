import re
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         print("OK")
         
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request,f'Account created for {username}!')
             print("OK2")
             return redirect('blog-home')

    else:
        print("OK3")
        form=UserRegisterForm()
    
    return render(request,'users/register.html',{
        'form':form,
        'title':"Register"
    })


