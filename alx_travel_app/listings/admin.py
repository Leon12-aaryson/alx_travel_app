from django.contrib import admin
from .models import Listing, Amenity, ListingAmenity


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Listing model.
    """
    list_display = ['title', 'location', 'price_per_night', 'availability', 'host', 'created_at']
    list_filter = ['availability', 'location', 'created_at']
    search_fields = ['title', 'description', 'location']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'location', 'host')
        }),
        ('Pricing & Availability', {
            'fields': ('price_per_night', 'availability')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    """
    Admin configuration for Amenity model.
    """
    list_display = ['name', 'icon']
    search_fields = ['name']
    ordering = ['name']


@admin.register(ListingAmenity)
class ListingAmenityAdmin(admin.ModelAdmin):
    """
    Admin configuration for ListingAmenity model.
    """
    list_display = ['listing', 'amenity']
    list_filter = ['amenity']
    search_fields = ['listing__title', 'amenity__name']
