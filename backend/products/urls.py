from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("/<int:pk>/", view=views.ProductDetailAPIview.as_view(), name="product-details-view")
]
