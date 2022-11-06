from django.urls import path
from . import views

# app_name="products"

urlpatterns = [
    path('products/', views.Products.as_view(), name='products'),
    path('products/<int:id>', views.ProductEdit.as_view(), name='product_edit'),
    path('user/create/', views.create_user, name='create_user'),
]
