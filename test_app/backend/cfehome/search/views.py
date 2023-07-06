from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer

from . import client

class SearchGenericView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None
        if not query:
            return Response("", status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)

