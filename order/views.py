from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from order.forms import OrderForm
from order.models import Order


@login_required()
def make_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'make_order.html', {'form': form})


@login_required()
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
