from . import views
from django.urls import path

urlpatterns = [
    path('', views.store, name='store'),
    # Views products by category
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    # Views product details
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
] 
