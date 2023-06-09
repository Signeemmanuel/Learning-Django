
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Articles
from .serializers import ArticleSerializer, UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    