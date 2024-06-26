from django.http import JsonResponse
from imp import reload
from .filters import ListingFilter
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Listing, LikedListing
from .forms import ListingForm,LocationForm

# Create your views here.

def main_view(request):
    return render(request, 'views/main.html', {"name" : 'AutoMax'})

@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    user_liked_listing= LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    liked_listings_ids = [li[0] for li in user_liked_listing]
    context = {
        'listing_filter':listing_filter,
        'liked_listings_ids':liked_listings_ids
    }
    return render(request, 'views/home.html', context)


@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm
    return render(request,'views/list.html',{'listing_form':listing_form,'location_form':location_form})


@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html', {'listing': listing, })
    except Exception:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home')
    

@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, request.FILES,instance=listing)
            location_form = LocationForm(request.POST,instance=listing.location)
            if listing_form.is_valid() and location_form.is_valid():
                location_form.save()
                listing_form.save()
                messages.success(request, "Listing updated successfully")
                return redirect('home')
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
    except Exception:
        messages.error(request, 'Error occured while updating the listing')
        return reload()
    return render(request, 'views/edit.html', {'listing_form':listing_form,'location_form':location_form})


@login_required
def like_listing_view(request,id):
    listing=get_object_or_404(Listing, id=id)
    liked_listing, created = LikedListing.objects.get_or_create(profile=request.user.profile, listing=listing)
    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
        
    return JsonResponse({
        'is_liked_by_user':created,
    })
    
    