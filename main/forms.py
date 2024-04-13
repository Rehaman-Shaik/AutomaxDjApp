from django import forms
from .models import Listing
from users.models import Location

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage', 'colour', 'description', 'engine', 'transmission', 'image'}

class LocationForm(forms.ModelForm):
    
    class Meta:
        model = Location
        fields = "__all__"