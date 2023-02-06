from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
 return render(request, 'home.html' )

def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            phone=form.cleaned_data['phone']
            if len(phone)==10:
                messages.success(request, 'Congratulations!! You have become an User.')
                user = form.save()
            else:
              messages.info(request,'please enter valid number')

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/')
  else:
   form = LoginForm()
  return render(request, 'login.html', {'form':form})
 else:
  return HttpResponseRedirect('/')
