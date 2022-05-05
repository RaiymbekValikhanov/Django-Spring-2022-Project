from django.urls import path, include
from .views import BaseUserViewSet, CustomerViewSet, PartnerViewSet, PartnersViewSet, PartnerProducts
from goods.views import ProductView

urlpatterns = [
    path('login/', include('users.login.urls')),
    path('partners/', PartnersViewSet.as_view({'get': 'list'})),
    path('user_info/', BaseUserViewSet.as_view({'get': 'list'})),
    path('customer_info/', CustomerViewSet.as_view({'get': 'list'})),
    path('partner_info/', PartnerViewSet.as_view({'get': 'list'})),
    path('partner_info/products/', PartnerProducts.as_view({'get': 'list', 'post': 'create'})),
    path('partner_info/products/<int:id>/', ProductView.as_view()),
]