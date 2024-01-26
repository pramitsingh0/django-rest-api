from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", view=views.product_alt_view, name="product-creation-view"),
    path("/<int:pk>/", view=views.product_alt_view, name="product-details-view"),
    path("/<int:pk>/update", view=views.ProductUpdateAPIview.as_view(), name="product-update-view"),
    path("/<int:pk>/delete", view=views.ProductDeleteAPIview.as_view(), name="product-delete-view"),
]
