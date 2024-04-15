from users.models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {"register_form" :register_form})
    
    
    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            # gets the new data from the db
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f"User {user.username} registered successfully")
            return redirect('home')
        else:
            return render(request, 'views/register.html', {"register_form" :register_form})
            #messages.error
            

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request,id):
        try:
            user = User.objects.get(id=id)
            profile = Profile.objects.get(user=user)
            context = {'user': profile.bio}
        except User.DoesNotExist:
            print(f"User with id {id} does not exist")
            context = {'user': 'Not found'}
        return render(request, 'views/profile.html', context)