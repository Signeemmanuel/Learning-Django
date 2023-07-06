from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
# from django.http import JsonResponse
from rest_framework.response import Response
from products.models import Product
# from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from .serializers import UserSerializer

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
        
        
class LoginAPIView(APIView):
    permission_classes=[]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            token, isCreated = Token.objects.get_or_create(user=user)
            return Response({
                "username": username,
                "token": str(token),
                }, status=200)
        
        return Response({"error": "Invalid credentials"}, status=401)
        
        
class RegisterAPIView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = make_password(serializer.validated_data["password"])
        user = serializer.save(password=password)            
        token = Token.objects.create(user=user)

        return Response({
            "username": username,
            "token": str(token) 
        }, status=200)
        