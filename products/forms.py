# from . models import Product
# from django import forms


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields='__all__'



from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = '__all__'

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),

            'unit': forms.Select(attrs={
                'class': 'form-select'
            }),

            'purchase_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter purchase price'
            }),

            'sale_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter sale price'
            }),

            'current_stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter stock quantity'
            }),

            'minimum_stock_alert': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimum stock alert'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

        }