from django.urls import path
from .views import CartView, UserOrdersView, UserOrderItemsView

urlpatterns = [
    path('my_cart/', CartView.as_view()),
    path('order_items/', UserOrderItemsView.as_view({'get': 'list', 'post': 'create'})),
]