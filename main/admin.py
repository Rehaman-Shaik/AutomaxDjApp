from .models import Listing
from django.contrib import admin

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Listing)