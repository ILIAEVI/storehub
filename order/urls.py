from django.urls import path
from order import views
from order.views import update_cart_item

urlpatterns = [
    path('checkout/', views.place_order, name='checkout'),
    path('order_list/', views.order_list, name='order_list'),
    path('add_cart_item/', views.add_cart_item, name='add_cart_item'),
    path('update_cart_item/<int:product_id>/', update_cart_item, name='update_cart_item'),
    path('delete_cart_item<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),
]
