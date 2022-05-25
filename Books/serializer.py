from dataclasses import field
from rest_framework import serializers
from .models import books
from core.serializer import UserSerializer
class BookSerializer(serializers.ModelSerializer):
    Book = serializers.CharField(source="get_libro_display")
    Type = serializers.CharField(source="get_type_display") 
    owner =  UserSerializer() 

    class Meta:
        model = books
        fields = "__all__"
        depth = 1

