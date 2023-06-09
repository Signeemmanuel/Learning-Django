from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Snippet
from .serailizers import SnippetSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    model = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    method = request.method()
    if method == 'GET':
        obj = Snippet.objects.all()
        serializer = SnippetSerializer(obj, many=True)
        return Response(serializer.data)
    elif method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        obj = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)