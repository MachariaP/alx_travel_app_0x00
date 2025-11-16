from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')
    host_id = serializers.ReadOnlyField(source='host.id')

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price_per_night',
            'location', 'max_guests', 'bedrooms', 'bathrooms',
            'created_at', 'updated_at', 'host', 'host_id'
        ]
        read_only_fields = ['created_at', 'updated_at', 'host', 'host_id']


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), source='listing', write_only=True
    )
    guest = serializers.ReadOnlyField(source='guest.username')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_id', 'guest',
            'check_in', 'check_out', 'total_price', 'created_at'
        ]
        read_only_fields = ['total_price', 'guest', 'created_at']
