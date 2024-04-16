from .models import Listing,LikedListing
from django.contrib import admin

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Listing)


class LikedListingAdmin(admin.ModelAdmin):
    pass
admin.site.register(LikedListing)