from django.urls import path
from . import views

app_name = "KaSheaCosmetics_catalog"

urlpatterns = [
    path("c/<slug:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("p/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
]
