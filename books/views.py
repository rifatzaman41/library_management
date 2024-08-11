from django.shortcuts import render,get_object_or_404
from .models import Book, Category

def book_list(request):
    category_id = request.GET.get('category')
    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'book_list.html', {'books': books, 'categories': categories})

def book_detail(self,request,book_id):
        book = get_object_or_404(Book,id=book_id)
        if book in book_detail:
             if book_id:
                  book=Book.objects.filter(book_id=book_id)
             else:
                  book=Book.objects.all()     
        return render(request,'book_detail.html', {'book':book})


