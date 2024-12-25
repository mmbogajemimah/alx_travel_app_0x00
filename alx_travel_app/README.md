# alx_travel_app_0x00 ReadMe

## 0. Database Modeling and Data Seeding in Django

### Objective

The goal of this project is to:
- Define database models.
- Create serializers for API data representation.
- Implement a management command to seed the database with sample data.

---

### Instructions

#### 1. Duplicate Project
Duplicate the existing project `alx_travel_app` to a new project directory named `alx_travel_app_0x00`.

---

#### 2. Create Models
In `listings/models.py`, define the following models:

- **Listing**:
  - Fields: `name`, `description`, `location`, `price_per_night`, `guest_capacity`, `amenities`, `host`, `created_at`, and `updated_at`.
  - Relationships: `host` as a `ForeignKey` to the `User` model.
  
- **Booking**:
  - Fields: `listing`, `guest_name`, `total_price`, `status`, `start_date`, `end_date`, and `created_at`.
  - Relationships: `listing` as a `ForeignKey` to the `Listing` model; `guest_name` as a `ForeignKey` to the `User` model.

- **Review**:
  - Fields: `listing`, `reviewer_name`, `rating`, `comment`, and `created_at`.
  - Relationships: `listing` as a `ForeignKey` to the `Listing` model; `reviewer_name` as a `ForeignKey` to the `User` model.
  - Constraints: `rating` must be between 1 and 5.

Ensure all fields have the appropriate data types, validators, and relationships.

---

#### 3. Set Up Serializers
In `listings/serializers.py`, create serializers for the models:

- **`ListingSerializer`**:
  - Includes fields: `id`, `name`, `description`, `location`, `price_per_night`, `guest_capacity`, `amenities`, `host`, `created_at`, and `updated_at`.

- **`BookingSerializer`**:
  - Includes fields: `id`, `listing`, `listing_name`, `guest_name`, `total_price`, `status`, `start_date`, `end_date`, and `created_at`.
  - Adds `listing_name` and `guest_name` as read-only fields for user-friendly display.

- **`ReviewSerializer`**:
  - Includes fields: `id`, `listing`, `listing_name`, `reviewer_name`, `rating`, `comment`, and `created_at`.
  - Adds `listing_name` and `reviewer_name` as read-only fields.

---

#### 4. Implement Seeders
Create a management command to seed the database:

- File: `listings/management/commands/seed.py`
- Functionality:
  - Populate the database with sample data for `Listing`, `Booking`, and `Review`.
  - Use Django ORM to create objects with meaningful default data.

---

#### 5. Run Seed Command
Test the seeder to ensure it works as expected:

1. Run the following command to populate the database:
   ```bash
   python manage.py seed
   ```

2. Verify that the database has been populated with sample data by querying the `Listing`, `Booking`, and `Review` models in the Django admin interface or via the Django shell.

---

### Project Notes

- Ensure models and serializers follow Django best practices.
- Validate that relationships and constraints are implemented correctly.
- The seed command should be idempotent (can be safely re-run without duplicating data).

---
