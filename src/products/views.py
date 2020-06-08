from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (CreateView, ListView, DeleteView, DetailView, UpdateView)
from django.urls import reverse

from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.
def product_create_view(request):
    # use initial for initialize data (initial = initial_data),
    initial_data = {
        "title": "Hello"
    }
    # for update existing object use instance for get object in form Product (instance= obj)
    # obj = Product.objects.get(id=6)
    # like this =>form = ProductForm(request.POST or None, initial = initial_data, instance=obj)
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     if request.method == "POST":
#         my_title = request.POST.get('title')
#         print(my_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#         my_form = RawProductForm()
#         if request.method == "POST":
#             my_form = RawProductForm(request.POST)
#             if my_form.is_valid():
#                 print(my_form.cleaned_data)
#                 Product.objects.create(**my_form.cleaned_data)
#                 my_form = RawProductForm()
#             else:
#                 print(my_form.errors)
# 
#         context= {
#             "form": my_form
#         }
#         return render(request, 'products/product_create.html', context)


# function base list view

def product_list_view(request):
    obj = Product.objects.all()
    # for one product by id => Product.objects.get(id=1)
    context = {
        'products': obj,
    }
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, product_id):
    # obj = Product.objects.get(id=product_id)
    # with 404 error handle if page DoesNOTExist
    obj = get_object_or_404(Product, id=product_id)

    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/products')

    context = {
        'form': form,
    }
    return render(request, 'products/product_detail.html', context)


def product_delete_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        obj.delete()
        return redirect('/products')

    context = {
        'object': obj,
    }
    return render(request, 'products/product_delete.html', context)


# class base list view

class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("products:product_list")


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    queryset = Product.objects.all()

    # we can also change key in object
    def get(self, request, *args, **kwargs):
        context = {'products': self.queryset}
        return render(request, self.template_name, context)


class ProductUpdateView(UpdateView):
    template_name = 'products/product_detail.html'
    form_class = ProductForm

    # for get particular obj from list by id on class based function
    def get_object(self, queryset=None):
        id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("products:product_list")


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'

    # for get particular obj from list by id on class based function
    def get_object(self, queryset=None):
        id = self.kwargs.get("product_id")
        return get_object_or_404(Product, id=id)

    def get_success_url(self):
        return reverse("products:product_list")
