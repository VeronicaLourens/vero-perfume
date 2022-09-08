from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
        views.order_history, name='order_history'),
    path('personal_details/', views.personal_details, name='personal_details'),
]