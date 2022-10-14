from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'),
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
    path(
        'remove_from_wishlist/<product_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist'),
]
