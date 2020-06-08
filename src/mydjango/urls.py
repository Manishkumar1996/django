"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view, about_view
from pages.views import (ContactView, HomeView, AboutView)
from products.views import product_list_view, product_detail_view, product_create_view, product_delete_view

urlpatterns = [
    # for products urls
    path('products/', include('products.urls')),

    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    # Functions base urls

    # path('', home_view, name='home'),
    # path('about/', about_view, name='about'),
    # path('contact/', contact_view, name='contact'),

    # path('product/create/', product_create_view, name='product_create'),
    # path('products/', product_list_view, name='products'),
    # path('product/<int:product_id>/', product_detail_view, name='product_update'),
    # path('product/<int:product_id>/delete/', product_delete_view, name='product_delete'),

    path('admin/', admin.site.urls, name='admin'),
]
