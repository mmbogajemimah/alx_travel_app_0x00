# listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id', 'name', 'description', 'location', 'price_per_night',
            'guest_capacity', 'amenities', 'host', 'created_at', 'updated_at'
        ]


class BookingSerializer(serializers.ModelSerializer):
    listing_name = serializers.ReadOnlyField(source='listing.name')
    guest_name = serializers.ReadOnlyField(source='guest_name.username')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_name', 'guest_name', 'total_price',
            'status', 'start_date', 'end_date', 'created_at'
        ]