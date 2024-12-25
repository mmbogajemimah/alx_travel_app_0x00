from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User
from decimal import Decimal
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with sample data for Listings, Bookings, and Reviews."

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample users
        self.stdout.write("Creating users...")
        users = []
        for _ in range(5):
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.email(),
                password="password123"
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f"Created {len(users)} users."))

        # Create sample listings
        self.stdout.write("Creating listings...")
        listings = []
        for _ in range(10):
            listing = Listing.objects.create(
                name=fake.company(),
                description=fake.text(),
                location=fake.address(),
                price_per_night=Decimal(random.randint(50, 500)),
                guest_capacity=random.randint(1, 10),
                amenities=fake.words(nb=5, unique=True),
                host=random.choice(users),
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year()
            )
            listings.append(listing)
        self.stdout.write(self.style.SUCCESS(f"Created {len(listings)} listings."))

        # Create sample bookings
        self.stdout.write("Creating bookings...")
        bookings = []
        for _ in range(15):
            booking = Booking.objects.create(
                listing=random.choice(listings),
                guest_name=random.choice(users),
                total_price=Decimal(random.randint(100, 2000)),
                status=random.choice(["pending", "confirmed", "cancelled"]),
                start_date=fake.date_this_month(),
                end_date=fake.date_this_month(),
                created_at=fake.date_time_this_year()
            )
            bookings.append(booking)
        self.stdout.write(self.style.SUCCESS(f"Created {len(bookings)} bookings."))

        # Create sample reviews
        self.stdout.write("Creating reviews...")
        reviews = []
        for _ in range(20):
            review = Review.objects.create(
                listing=random.choice(listings),
                reviewer_name=random.choice(users),
                rating=random.randint(1, 5),
                comment=fake.text(),
                created_at=fake.date_time_this_year()
            )
            reviews.append(review)
        self.stdout.write(self.style.SUCCESS(f"Created {len(reviews)} reviews."))

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully."))
