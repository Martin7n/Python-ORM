import os
from datetime import date, timedelta

import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Song, Artist, Review, Product, Driver, DrivingLicense, Owner, Car, \
    Registration


# Create queries within functions


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by("id")
    result = []
    for author in authors:
        author_books = author.book_set.all()
        if author_books:
            result.append(f"{author.name} has written - {', '.join(b.title for b in author_books)}!")
                # print(', '.join(str(x.title) for x in author_books))
    return '\n'.join(result)

# print(show_all_authors_with_their_books())

def delete_all_authors_without_books():
    # authors = Author.objects.all()
    # for author in authors:
    #     if author.book_set.all().count() == 0:
    #         author.delete()
    Author.objects.filter(book__isnull=True).delete()

# delete_all_authors_without_books()


##test code 1


#
# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )
#
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)
#
# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())

def add_song_to_artist(artist_name: str, song_title: str):
    the_artist = Artist.objects.get(name=artist_name)
    the_song = Song.objects.get(title=song_title)
    the_artist.songs.add(the_song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')

def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


#
#
# ##test code 2
# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")
#
# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")
#
# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")
#
# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


def calculate_average_rating_for_product_by_name(product_name: str):
    #product = Product.objects.filter(name=product_name).get()
    product = Product.objects.get(name=product_name)

    ratings = product.reviews.all()
    if ratings:
        return sum(r.rating for r in ratings)/len(ratings)

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')

# print(get_products_with_no_reviews())

def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()

#
# # Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)
# #
# # # Run the function to get products without reviews
# # products_without_reviews = get_products_with_no_reviews()
# # print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
#
# # Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
#
# # Calculate and print the average rating
# print(calculate_average_rating_for_product_by_name("Laptop"))



def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by('-license_number')

    return ('\n'.join(f"License with number: {license.license_number} expires on {license.issue_date+timedelta(365)}!" for license in licenses))


def get_drivers_with_expired_licenses(due_date: date):
    licenses = DrivingLicense.objects.all()
    result = []
    for license in licenses:
        expiration_date = license.issue_date + timedelta(365)
        if expiration_date > due_date:
            result.append(license.driver)
    return result
    # print ('\n'.join(str(x.issue_date) for x in result))
# def get_drivers_with_expired_licenses(due_date: date) -> str:
#     expiration_cutoff_date = due_date - timedelta(days=365)
#
#     drivers_with_expired_licenses = Driver.objects.filter(
#         license__issue_date__gt=expiration_cutoff_date,
#     )
#
#     return drivers_with_expired_licenses


# get_drivers_with_expired_licenses(date(2023, 1, 1))
#
#  # Create drivers
# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# # Create licenses associated with drivers
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
#
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)

#
# # Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
#
#
# #
# #
# # # Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
#
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")



def register_car_by_owner(owner: Owner):
    reg = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()
    car.owner = owner
    car.save()
    reg.registration_date = date.today()
    reg.car = car
    reg.save()
    return f"Successfully registered {car.model} to {owner.name} with registration number {reg.registration_number}."


#
# def register_car_by_owner(owner: Owner):
#     registration_not_related_to_car = Registration.objects.filter(car__isnull=True).first()
#     car_without_registration = Car.objects.filter(registration__isnull=True).first()
#
#     if registration_not_related_to_car and car_without_registration:
#         car_without_registration.registration = registration_not_related_to_car
#         registration_not_related_to_car.registration_date = date.today()
#
#         car_without_registration.save()
#         registration_not_related_to_car.save()
#
#         return f"Successfully registered {car_without_registration.model} to {owner.name} with registration " \
#                f"number {registration_not_related_to_car.registration_number}."
# ##Test code:
#
# #
# #
# # Create owners
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')
#
# # Create cars
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')

print(register_car_by_owner(owner1))
