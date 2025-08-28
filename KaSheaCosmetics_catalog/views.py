from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product


class CategoryListView(ListView):
    template_name = "catalog/category_list.html"
    context_object_name = "categories"
    queryset = Category.objects.filter(
        is_active=True, parent__isnull=True
    ).prefetch_related("children")


class CategoryDetailView(DetailView):
    template_name = "catalog/category_detail.html"
    context_object_name = "category"
    model = Category
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["products"] = self.object.products.filter(is_active=True)
        return ctx


class ProductDetailView(DetailView):
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    model = Product
    slug_field = "slug"
    slug_url_kwarg = "slug"
