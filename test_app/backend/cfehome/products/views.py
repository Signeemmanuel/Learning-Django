from rest_framework import generics, authentication, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
# from api.permissions import IsStaffEditorPermission
from api.mixins import IsStaffEditorPermissionMixin, UserQuerySetMixin
# Create your views here.

class ProductListCreateAPIView(UserQuerySetMixin, IsStaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')      
        # content = serializer.validated_data.get('content')
        # if content is None:
        #     serializer.save(content=title)
        content = serializer.validated_data.get('content', title)
        serializer.save(user=self.request.user, content=content)
            
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)
    
class ProductDetails(UserQuerySetMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdate(UserQuerySetMixin, IsStaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            
class ProductDestroy(UserQuerySetMixin, IsStaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

@api_view(['GET', 'POST'])
def product_all_views(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # Detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        # List View
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                serializer.save(content=title)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)