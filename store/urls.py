from django.urls import path
from store import views

urlpatterns = [
    path('products/add/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
]
