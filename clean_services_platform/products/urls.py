from django.urls import path
from . import views  # Import product views

app_name = 'products'  # Set the application namespace to 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('<int:product_id>/', views.product_detail, name='product_detail'), # Add a URL pattern for product detail, remember to update later
    # path('create/', views.product_create, name='product_create'), # Add a URL pattern for product creation, remember to update later
    # path('<int:product_id>/update/', views.product_update, name='product_update'),
    # path('<int:product_id>/delete/', views.product_delete, name='product_delete'),
    # path('<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    # path('<int:product_id>/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/checkout/', views.cart_checkout, name='cart_checkout'),
    # path('cart/checkout/success/', views.cart_checkout_success, name='cart_checkout_success'),
    # path('cart/checkout/cancel/', views.cart_checkout_cancel, name='cart_checkout_cancel'),
]