"""Catalogue serializer class"""
from rest_framework import serializers
from ..models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    """Book serializer class"""
    class Meta:
        """Modeling from the Book model class"""
        model = Book
        fields = ["id","category","title","description","available","image"]

class CategorySerializer(serializers.ModelSerializer):
    """Category serializer class"""
    class Meta:
        """Serializing from Category Model class"""
        model = Category
        fields = ["id","name"]
