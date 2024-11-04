from django import forms
from store.models import Product


class ProductFilterForm(forms.Form):
    q = forms.CharField(required=False, label='Search', max_length=100)
    price = forms.DecimalField(required=False, min_value=0, max_value=1000)
    discount_filter = forms.BooleanField(required=False, label='Discount')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
