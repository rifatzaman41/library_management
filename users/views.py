from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from .models import UserProfile, BorrowedBook
from books.models import Book
from django.utils import timezone
from decimal import Decimal
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('book_list')

def deposit_money(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        request.user.userprofile.balance += Decimal(amount)
        request.user.userprofile.save()
        send_mail('Deposit Successful', f'You have successfully deposited {amount} taka.', 'from@example.com', [request.user.email])
        return redirect('profile')
    return render(request, 'deposite_money.html')

def borrow_book(self,request,borrow_id):
    book = get_object_or_404(BorrowedBook,id=borrow_id)
    if request.user.userprofile.balance >= book.borrowing_price:
        request.user.userprofile.balance -= book.borrowing_price
        request.user.userprofile.save()
        BorrowedBook.objects.create(user=request.user, book=book)
        send_mail('Borrowing Successful', f'You have successfully borrowed {book.title}.', 'from@example.com', [request.user.email])
        return redirect('profile')
    else:
        return render(request, 'borrow_book.html', {'error': 'Insufficient balance'})

def return_book(self,request,return_id):
    borrowed_book = get_object_or_404(BorrowedBook,id=return_id)
    borrowed_book.returned_at = timezone.now()
    borrowed_book.save()
    request.user.userprofile.balance += borrowed_book.book.borrowing_price
    request.user.userprofile.save()
    send_mail('Return Successful', f'You have successfully returned {borrowed_book.book.title}.', 'from@example.com', [request.user.email])
    return redirect('profile')

def profile(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'profile.html', {'borrowed_books': borrowed_books})
