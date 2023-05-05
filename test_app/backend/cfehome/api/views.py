
from rest_framework.decorators import api_view
# from django.http import JsonResponse
from rest_framework.response import Response
from products.models import Product
# from django.forms.models import model_to_dict
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    get_data = {}
    if instance:
        # data = model_to_dict(model_data, fields=["id", "content"])
        get_data = ProductSerializer(instance).data
    return Response(get_data)

@api_view(["POST"])
def api_post(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
        
        