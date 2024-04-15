from django import forms
from django.contrib.auth.models import User
from .models import Location, Profile



class UserForm(forms.ModelForm):
    username= forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name'}
        
class ProfieForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= {'bio', 'photo','phone_number'}
        
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"