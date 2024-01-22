from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    path("", views.api_home, name="home"),
    path("products/create", views.create_product, name="create_product"),
]
