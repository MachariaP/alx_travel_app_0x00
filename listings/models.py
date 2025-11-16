from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Listing(models.Model):
    """A property that can be booked."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    location = models.CharField(max_length=255)
    max_guests = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    bedrooms = models.PositiveSmallIntegerField(default=1)
    bathrooms = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listings'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Listings'

    def __str__(self):
        return f"{self.title} – {self.location}"


class Booking(models.Model):
    """A reservation for a Listing."""
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bookings'
    )
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'check_in', 'check_out')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.guest} – {self.listing.title} ({self.check_in} → {self.check_out})"


class Review(models.Model):
    """A review written by a guest for a Booking."""
    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, related_name='review'
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review {self.rating}★ for {self.booking}"
