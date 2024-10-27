from django.urls import path
from store import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('store/categories/', views.CategoryListView.as_view(), name='category_list'),
    path('store/categories/<int:category_id>/', views.CategoryListView.as_view(), name='category_list'),
    path('store/products/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),

]
