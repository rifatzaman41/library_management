from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from   .models import UserProfile,BorrowedBook
class UserRegistrationForm(UserCreationForm):
    balance = forms.DecimalField(max_length=10)
    book_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'balance','book_name']
     

    def save(self, commit=True):
        our_user = super().save(commit=False) 
        if commit == True:
            our_user.save()
            balance = self.cleaned_data.get('balance')
            book_name=self.cleaned_data.get('book_name')

            UserProfile.objects.create(
            user=our_user,
            balance=balance
            )
            BorrowedBook.objects.create(
            user=our_user,
            book_name=book_name
            )

        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
  

class UserUpdateForm(forms.ModelForm):
    balance = forms.DecimalField(max_length=10)
    book_name = forms.CharField(max_length=100) 

    class Meta:
        model = User
        fields = ['username', 'balance','book_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
