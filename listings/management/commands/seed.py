import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from listings.models import Listing, Booking

User = get_user_model()


FAKER_LOCATIONS = [
    "Nairobi, Kenya", "Mombasa, Kenya", "Kisumu, Kenya",
    "Nakuru, Kenya", "Eldoret, Kenya", "Nyeri, Kenya",
    "Machakos, Kenya", "Thika, Kenya", "Kakamega, Kenya",
    "Meru, Kenya"
]

TITLES = [
    "Cozy Apartment in City Center",
    "Beachfront Villa with Pool",
    "Mountain Cabin Retreat",
    "Luxury Penthouse Suite",
    "Budget Studio Near University",
    "Family House with Garden",
    "Modern Loft Downtown",
    "Rustic Farmhouse Experience",
    "Seaside Bungalow",
    "Executive Suite with View"
]

DESCRIPTIONS = [
    "Enjoy a comfortable stay with all amenities.",
    "Perfect for a romantic getaway or family vacation.",
    "Stunning views and easy access to local attractions.",
    "Fully equipped kitchen, Wi-Fi, and parking included.",
    "Walking distance to shops, restaurants, and public transport."
]


class Command(BaseCommand):
    help = "Seed the database with sample Listings and Bookings"

    def add_arguments(self, parser):
        parser.add_argument(
            '--listings', type=int, default=15,
            help='Number of listings to create (default: 15)'
        )
        parser.add_argument(
            '--bookings', type=int, default=30,
            help='Number of bookings to create (default: 30)'
        )

    def handle(self, *args, **options):
        self.stdout.write("Starting seeding...")

        # Ensure users exist
        host, _ = User.objects.get_or_create(
            username='host_demo',
            defaults={'email': 'host@demo.com', 'is_staff': False}
        )
        guest, _ = User.objects.get_or_create(
            username='guest_demo',
            defaults={'email': 'guest@demo.com'}
        )

        # ---- Create Listings (one by one to get IDs) ----
        created_listings = 0
        for _ in range(options['listings']):
            listing = Listing(
                title=random.choice(TITLES),
                description=random.choice(DESCRIPTIONS),
                price_per_night=round(random.uniform(30, 500), 2),
                location=random.choice(FAKER_LOCATIONS),
                max_guests=random.randint(1, 8),
                bedrooms=random.randint(1, 5),
                bathrooms=random.randint(1, 3),
                host=host
            )
            listing.save()  # ← This gives it an ID
            created_listings += 1

        self.stdout.write(
            self.style.SUCCESS(f"Created {created_listings} listings")
        )

        # ---- Create Bookings ----
        created_bookings = 0
        all_listings = Listing.objects.all()

        for _ in range(options['bookings']):
            listing = random.choice(all_listings)
            nights = random.randint(1, 14)
            check_in = timezone.now().date() + timedelta(days=random.randint(1, 60))
            check_out = check_in + timedelta(days=nights)

            # Avoid duplicate booking dates
            if Booking.objects.filter(
                listing=listing,
                check_in=check_in,
                check_out=check_out
            ).exists():
                continue

            Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in=check_in,
                check_out=check_out,
                total_price=listing.price_per_night * nights
            )
            created_bookings += 1

        self.stdout.write(
            self.style.SUCCESS(f"Created {created_bookings} bookings")
        )
        self.stdout.write(self.style.SUCCESS("Seeding completed!"))
