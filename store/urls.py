from django.urls import path
from store import views

urlpatterns = [
    # path('store/add-product', views.add_product, name='add_product'),
    # path('store/products/', views.product_list, name='product_list'),
    # path('store/categories/', views.category_list, name='category_list'),
    # path('store/product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('store/categories/', views.categories, name='category_list'),
    path('store/categories/<int:category_id>/products/', views.categories, name='category_detail'),
    path('store/products/<int:product_id>/', views.product_detail, name='product_detail'),

]
