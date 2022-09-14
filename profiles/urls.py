from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'),
    path(
        'personal_details/',
        views.personal_details,
        name='personal_details'),
    path(
        'delete_profile/',
        views.delete_profile,
        name='delete_profile'),
    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'),
    path(
        'add_to_wishlist/<int:product_id>',
        views.add_to_wishlist,
        name='add_to_wishlist'),
]
