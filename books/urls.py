from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('book_detail/<int:book_id>/', book_detail, name='book_detail'),
    
]
