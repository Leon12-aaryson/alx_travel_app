from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, AmenityViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'amenities', AmenityViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
