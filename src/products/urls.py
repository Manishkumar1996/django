from django.urls import path
from .views import (ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView)

app_name = 'products'
urlpatterns = [
    # Class base urls
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:product_id>/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
