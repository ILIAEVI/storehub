from django.core.management.base import BaseCommand
from django.db.models import Count
from store.models import Product
from order.models import UserCart, CartItem


class Command(BaseCommand):
    help = 'Find most popular products'

    def handle(self, *args, **options):
        popular_products = (CartItem.objects
                            .values('product')
                            .annotate(
            unique_users=Count('cart__user', distinct=True))
                            .order_by('-unique_users')[:3])

        if popular_products:
            self.stdout.write(self.style.SUCCESS('Top 3 Most Popular Products:'))
            for item in popular_products:
                product = Product.objects.get(id=item['product'])
                self.stdout.write(f"Product: {product.name}, Unique quantity: {item['unique_users']}")
        else:
            self.stdout.write(self.style.WARNING('No products found in carts.'))





