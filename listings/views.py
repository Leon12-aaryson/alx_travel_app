from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Listing, Amenity
from .serializers import ListingSerializer, ListingDetailSerializer, AmenitySerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing travel listings.
    
    Provides CRUD operations for travel listings with filtering and search capabilities.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['location', 'availability', 'price_per_night']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price_per_night', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the action.
        """
        if self.action == 'retrieve':
            return ListingDetailSerializer
        return ListingSerializer
    
    def perform_create(self, serializer):
        """
        Save the listing with the current user as host.
        """
        serializer.save(host=self.request.user)
    
    @swagger_auto_schema(
        method='post',
        operation_description="Mark a listing as unavailable",
        responses={200: "Listing marked as unavailable"}
    )
    @action(detail=True, methods=['post'])
    def mark_unavailable(self, request, pk=None):
        """
        Mark a listing as unavailable.
        """
        listing = self.get_object()
        listing.availability = False
        listing.save()
        return Response({'status': 'Listing marked as unavailable'})
    
    @swagger_auto_schema(
        method='post',
        operation_description="Mark a listing as available",
        responses={200: "Listing marked as available"}
    )
    @action(detail=True, methods=['post'])
    def mark_available(self, request, pk=None):
        """
        Mark a listing as available.
        """
        listing = self.get_object()
        listing.availability = True
        listing.save()
        return Response({'status': 'Listing marked as available'})


class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing amenities.
    
    Provides read-only access to amenities.
    """
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [permissions.AllowAny]
