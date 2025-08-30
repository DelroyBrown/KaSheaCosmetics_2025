# views.py
from django.shortcuts import render
from django.db.models import Prefetch
from KaSheaCosmetics_catalog.models import Product, ProductImage

def home(request):
    img_qs = ProductImage.objects.order_by('-is_primary', 'sort_order', 'id')

    featured_products = (
        Product.objects
        .filter(featured=True, is_active=True)
        .prefetch_related(Prefetch('images', queryset=img_qs, to_attr='imgs'))[:4]
    )

    return render(request, "home.html", {"featured_products": featured_products})
