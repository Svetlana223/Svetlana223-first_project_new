from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user_orders_view, name='user-orders'),
    path('product/create/', views.product_create, name='product_create'),
]

