from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Listing, Amenity


class ListingModelTest(TestCase):
    """
    Test cases for Listing model.
    """
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.listing = Listing.objects.create(
            title='Test Listing',
            description='A test listing',
            location='Test City',
            price_per_night=100.00,
            host=self.user
        )
    
    def test_listing_creation(self):
        """Test that a listing can be created successfully."""
        self.assertEqual(self.listing.title, 'Test Listing')
        self.assertEqual(self.listing.host, self.user)
        self.assertTrue(self.listing.availability)
    
    def test_listing_str_representation(self):
        """Test the string representation of a listing."""
        self.assertEqual(str(self.listing), 'Test Listing')


class ListingAPITest(APITestCase):
    """
    Test cases for Listing API endpoints.
    """
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.listing = Listing.objects.create(
            title='Test Listing',
            description='A test listing',
            location='Test City',
            price_per_night=100.00,
            host=self.user
        )
    
    def test_get_listing_list(self):
        """Test retrieving a list of listings."""
        url = reverse('listing-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_get_listing_detail(self):
        """Test retrieving a specific listing."""
        url = reverse('listing-detail', kwargs={'pk': self.listing.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Listing')
    
    def test_create_listing_authenticated(self):
        """Test creating a listing when authenticated."""
        self.client.force_authenticate(user=self.user)
        url = reverse('listing-list')
        data = {
            'title': 'New Listing',
            'description': 'A new test listing',
            'location': 'New City',
            'price_per_night': 150.00
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Listing.objects.count(), 2)
    
    def test_create_listing_unauthenticated(self):
        """Test creating a listing when not authenticated."""
        url = reverse('listing-list')
        data = {
            'title': 'New Listing',
            'description': 'A new test listing',
            'location': 'New City',
            'price_per_night': 150.00
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
