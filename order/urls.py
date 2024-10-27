from django.urls import path
from order import views

urlpatterns = [
    path('checkout/', views.PlaceOrderView.as_view(), name='checkout'),
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('add_cart_item/', views.AddCartItemView.as_view(), name='add_cart_item'),
    path('update_cart_item/<int:product_id>/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('delete_cart_item<int:product_id>/', views.DeleteCartItemView.as_view(), name='delete_cart_item'),
]
