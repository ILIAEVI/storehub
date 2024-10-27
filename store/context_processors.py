from order.models import UserCart


def cart_items_total_quantity(request):
    if request.user.is_authenticated:
        user_cart = UserCart.objects.filter(user=request.user).first()
        total_quantity = sum(item.quantity for item in user_cart.items.all()) if user_cart else 0

        if user_cart:
            return {'total_quantity': total_quantity}

    return {
        'total_quantity': 0,
    }
