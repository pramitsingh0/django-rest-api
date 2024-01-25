from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", view=views.product_alt_view, name="product-creation-view"),
    path("/<int:pk>/", view=views.product_alt_view, name="product-details-view"),
]
