from . models import Supplier
from django import forms

class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Supplier name'
            }),

            'phone':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Supplier phone'
            }),

            'address':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Supplier address'
            }),
            'opening_balance':forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter opening balance'
            }) ,     
            'notes':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Supplier notes'
            }),                  

        }



#   python manage.py runserver        