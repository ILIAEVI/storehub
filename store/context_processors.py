from order.models import UserCart


def cart_items_total_quantity(request):
    user_cart = UserCart.objects.filter(user=request.user).first()
    total_quantity = sum(item.quantity for item in user_cart.items.all()) if user_cart else 0

    return {
        'total_quantity': total_quantity,
    }
