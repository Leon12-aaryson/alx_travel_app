from rest_framework import serializers
from .models import Listing, Amenity, ListingAmenity


class AmenitySerializer(serializers.ModelSerializer):
    """
    Serializer for Amenity model.
    """
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'icon']


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listing model.
    """
    host = serializers.StringRelatedField(read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'location', 
            'price_per_night', 'availability', 'created_at', 
            'updated_at', 'host', 'amenities'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'host']
    
    def create(self, validated_data):
        """
        Create a new listing with the current user as host.
        """
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['host'] = request.user
        return super().create(validated_data)


class ListingDetailSerializer(ListingSerializer):
    """
    Detailed serializer for Listing model with additional fields.
    """
    amenities = AmenitySerializer(many=True, read_only=True)
    
    class Meta(ListingSerializer.Meta):
        fields = ListingSerializer.Meta.fields + ['amenities']
