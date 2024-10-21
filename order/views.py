from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def place_order(request):
    return render(request, 'checkout.html')

def order_list(request):
    return render(request, 'cart.html')