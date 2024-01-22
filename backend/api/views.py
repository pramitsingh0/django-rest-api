import json

# from django.http import JsonResponse
from products.models import Product

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# Create your views here.
#
#
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    django rest framework API view
    """
    instance = Product.objects.last()
    data = ProductSerializer(instance).data

    return Response(data)


@api_view(["POST"])
def create_product(request, *args, **kwargs):
    product_serializer = ProductSerializer(data=request.data)
    data = {}
    if product_serializer.is_valid(raise_exception=True):
        product_serializer.save()
        data = product_serializer.data
        return Response(data)
    return Response({"error": "Invalid Data"}, status=401)
