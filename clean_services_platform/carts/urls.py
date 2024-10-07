from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.carts, name='carts/carts.html'),
    # path('<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    # path('<int:product_id>/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/checkout/', views.cart_checkout, name='cart_checkout'),
    # path('cart/checkout/success/', views.cart_checkout_success, name='cart_checkout_success'),
    # path('cart/checkout/cancel/', views.cart_checkout_cancel, name='cart_checkout_cancel'),
]