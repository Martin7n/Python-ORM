import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product
from django.db.models import Count, Q, F


# Create queries within functions

#
# reg = Profile.objects.annotate(count_profiles=Count('orders_profile')).filter(count_profiles__gte=2)
# for r in reg:
#     print(r)

# a = Profile.objects.get_regular_customers()
# print(a)

##Django Queries I
def get_profiles(search_string=None):
    if search_string is None:
        return ""
    query = Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)
    profiles = Profile.objects.filter(query).annotate(num_ord=Count("orders_profile")).order_by('full_name')

    if not profiles.exists():
        return ""
    return '\n'.join(f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.num_ord}" for p in profiles)


# print(get_profiles(None))


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()
    # profiles = Profile.objects.annotate(
    #         count_profiles=Count('orders_profile')
    #     ).filter(count_profiles__gt=2).order_by('-count_profiles')
    # return '\n'.join(f"{profile.full_name}" for profile in profiles)
    if not profiles:
        return ""
    return '\n'.join(f"Profile: {profile.full_name}, orders: {profile.count_profiles}" for profile in profiles)

# print(get_loyal_profiles())

def get_last_sold_products():
    last_sold_products = Order.objects.last()
    if not Order.objects.all() or not last_sold_products.products.all():
        return ""
    return '\n'.join(f"Last sold products: {product.name}" for product in last_sold_products.products.all())
#
# print(get_last_sold_products()).


###Django Queries II

def get_top_products():
    products = Product.objects.annotate(count_of=Count('orders_products')).filter(count_of__gt=0).order_by('-count_of')[:5]
    result = []
    if not products:
        return ""
    for prod in products:
        result.append(f"\n{prod.name}, sold {prod.count_of} times")
    if not result:
        return ""
    return f"Top products:{''.join(result)}"

# print(get_top_products())

def apply_discounts():
    more_than_two_products_ordered_object = Order.objects.annotate(count_prod=Count("products")).filter(count_prod__gt=2, is_completed=False)
    if not more_than_two_products_ordered_object:
        return ""
    discounted = more_than_two_products_ordered_object.update(total_price = F('total_price')*0.9)
    return f"Discount applied to {more_than_two_products_ordered_object.count()} orders."

# print(apply_discounts())

def complete_order():


    order = Order.objects.filter(is_completed=False).first()
    if not order or not Order.objects.all():
        return ""


    for product in order.products.all():
        if product.is_available:
            product.in_stock -= 1
            if product.in_stock ==0:
                product.is_available = False
            product.save()
    order.is_completed = True
    order.save()
    return "Order has been completed!"

# print(complete_order())
