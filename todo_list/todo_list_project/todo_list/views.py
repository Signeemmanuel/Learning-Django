from rest_framework import generics
from .models import TodoItems
from .serializers import TodoItemSerializer

# Create your views here.
class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItems.objects.all()
    serializer_class = TodoItemSerializer
    

class TodoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItems
    serializer_class = TodoItemSerializer