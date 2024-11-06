from django.urls import path

from .views import Index, ShopView, ProductByCategory

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('<int:pk>/', Index.as_view(), name='home'),
    path('products/shop/', ShopView.as_view(), name='shop'),
    path('products/shop/<slug:slug>/', ProductByCategory.as_view(), name='product_by_category'),
]