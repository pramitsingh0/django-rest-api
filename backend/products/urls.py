from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", view=views.ProductCreateAPIview.as_view(), name="product-creation-view"),
    path("/<int:pk>/", view=views.ProductDetailAPIview.as_view(), name="product-details-view")
]
