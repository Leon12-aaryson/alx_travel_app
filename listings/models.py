from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    """
    Model representing a travel listing.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Travel Listing'
        verbose_name_plural = 'Travel Listings'
    
    def __str__(self):
        return self.title


class Amenity(models.Model):
    """
    Model representing amenities available in listings.
    """
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name_plural = 'Amenities'
    
    def __str__(self):
        return self.name


class ListingAmenity(models.Model):
    """
    Through model for many-to-many relationship between Listing and Amenity.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('listing', 'amenity')
        verbose_name = 'Listing Amenity'
        verbose_name_plural = 'Listing Amenities'
