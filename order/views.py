from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, View
from order.models import CartItem, UserCart
from store.models import Product


class PlaceOrderView(TemplateView):
    template_name = 'checkout.html'


class OrderListView(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart_items'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            cart = user.user_cart
            return CartItem.objects.filter(cart=cart)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.request.user.user_cart
        return context


class AddCartItemView(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = get_object_or_404(Product, id=product_id)

        if product.quantity == 0:
            messages.error(request, "This product is out of stock.")
            return redirect('category_list')

        cart, created = UserCart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            if cart_item.quantity + 1 > product.quantity:
                messages.error(request, "There is not enough stock available to add more of this product.")
                return redirect('order_list')
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1

        cart_item.save()

        return redirect('order_list')


class UpdateCartItemView(View):
    def post(self, request, product_id, *args, **kwargs):
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


class DeleteCartItemView(View):
    def post(self, request, product_id, *args, **kwargs):
        cart_item = get_object_or_404(CartItem, cart__user=request.user, product_id=product_id)
        cart_item.delete()
        return redirect('order_list')
