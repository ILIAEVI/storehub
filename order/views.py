from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from order.models import CartItem, UserCart
from store.models import Product


def place_order(request):
    return render(request, 'checkout.html')

def order_list(request):
    user = request.user
    cart = user.user_cart
    cart_items = CartItem.objects.filter(cart=cart)

    paginator = Paginator(cart_items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'cart': cart,
    }

    return render(request, 'cart.html', context)

def add_cart_item(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = get_object_or_404(Product, id=product_id)

        if product.quantity == 0:
            messages.error(request, "This product is out of stock.")
            return redirect('category_list')

        cart, created = UserCart.objects.get_or_create(user=request.user)
        cart_item , created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            if cart_item.quantity + 1 > product.quantity:
                messages.error(request, "There is not enough stock available to add more of this product.")
                return redirect('order_list')
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1

        cart_item.save()

    return redirect('order_list')


def update_cart_item(request, product_id):
    if request.method == 'POST':

        cart_item = get_object_or_404(CartItem, cart__user=request.user, product_id=product_id)
        action = request.POST['action']

        if action == 'increase':
            if cart_item.product.quantity + 1 > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()
            else:
                messages.error(request, "There is no more product in stock.")
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

        return redirect('order_list')

    return redirect('order_list')

def delete_cart_item(request, product_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, cart__user=request.user, product_id=product_id)
        cart_item.delete()
    return redirect('order_list')
