from django.urls import path
from . views import ProductView, CartView

urlpatterns = [
    path('product/', ProductView.as_view(), name='product_view'),
    path('cart/', CartView.as_view(), name='cart_view')
]