from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Listing
class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    guest_capacity = models.IntegerField()
    amenities = models.CharField(max_length=255)
    host = models.ForeignKey()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.name


# Booking
class Booking(models.Model):
    STATUS_TYPES = {
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    }
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='booking_listing')
    guest_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings_user")
    total_price = models.DecimalField()
    status = models.CharField(max_length=20, choices=STATUS_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.guest_name} - {self.listing.name}"


# Review
class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="review_listing")
    reviewer_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_user")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.reviewer_name} - {self.listing.name} ({self.rating}/5)"