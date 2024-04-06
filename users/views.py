from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,f'Your are logged in as {username}')
                return redirect('home')
            else :
                pass
                #messages.error(request,f'Unable to login ')
        #else :
            #messages.error(request,f'Unable to login ')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form':login_form})


def register_view(request):
    register_form = UserCreationForm()
    return render(request, 'views/register.html' ,{'register_form' : register_form})


class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {"register_form" :register_form})
    
    
    def post(self, request):
        pass