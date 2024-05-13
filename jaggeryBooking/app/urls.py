from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name=''),
    path('<int:year>/<str:month>/', Home, name=''),
    path('cart/', Cart, name='cart'),
    path('register/', register, name='register'),
    path("book-slots/", bookslots, name='book-slots')
]