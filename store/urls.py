from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('store/categories/', views.categories, name='category_list'),
    path('store/categories/<int:category_id>/', views.categories, name='category_list'),
    path('store/products/<int:product_id>/', views.product_detail, name='product_detail'),

]
