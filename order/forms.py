from django import forms
from order.models import Order
from store.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(),
        }