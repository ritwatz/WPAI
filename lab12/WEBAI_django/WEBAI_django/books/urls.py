from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list, name='book_list'),
    path('insert_book/', views.insert_book, name='insert_book'),
    path('insert/', views.book_input, name='book_input'),
]