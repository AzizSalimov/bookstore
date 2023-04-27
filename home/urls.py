from django.urls import path
from .views import home, bookstore

urlpatterns = [
    path('', home, name='home'),
    path('bookstore/', bookstore, name = 'bookstore')
]