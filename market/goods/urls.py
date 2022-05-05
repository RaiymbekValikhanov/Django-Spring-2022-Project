from django.urls import path
from .views import get_all_products, get_all_categories, ProductView, CategoryView

urlpatterns = [
    path('products/', get_all_products),
    path('categories/', get_all_categories),
    path('products/<int:id>/', ProductView.as_view()),
    path('categories/<int:id>/', CategoryView.as_view()),

]