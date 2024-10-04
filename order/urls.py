from django.urls import path
from order import views


urlpatterns = [
    path('make-order/', views.make_order, name='make_order'),
    path('list/', views.order_list, name='order_list'),
]
