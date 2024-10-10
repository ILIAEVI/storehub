from django.urls import path
from store import views

urlpatterns = [
    path('add-product', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),

]
