from django.urls import path
from .views import register, user_login, user_logout, deposit_money, borrow_book, return_book, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('deposit/', deposit_money, name='deposit'),
    path('borrow/<int:borrow_id>/', borrow_book, name='borrow_book'),
    path('return/<int:return_id>/', return_book, name='return_book'),
    path('profile/', profile, name='profile'),
]
