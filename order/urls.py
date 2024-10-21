from django.urls import path
from order import views


urlpatterns = [
    path('checkout/', views.place_order, name='checkout'),
    path('order_list/', views.order_list, name='order_list'),
]
