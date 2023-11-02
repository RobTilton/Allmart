from django.urls import path
from . import views



urlpatterns = [
    path('storefront/', views.Storefront, name='home'),
]