from rest_framework import serializers
from .models import TodoItems

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItems
        fields = '__all__'