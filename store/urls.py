from django.urls import path
from store import views

urlpatterns = [
    path('add-product', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),

    path('categories/<int:category_id>/products/', views.category_detail, name='category_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]
