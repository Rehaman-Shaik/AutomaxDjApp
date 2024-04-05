from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def main_view(request):
    return render(request, 'views/main.html', {"name" : 'AutoMax'})

@login_required
def home_view(request):
    print(request.user.username)
    return render(request, 'views/home.html')