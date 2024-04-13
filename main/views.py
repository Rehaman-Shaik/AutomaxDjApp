from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Listing

# Create your views here.

def main_view(request):
    return render(request, 'views/main.html', {"name" : 'AutoMax'})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    return render(request, 'views/home.html', {'listings' :listings})


@login_required
def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'views/list.html')