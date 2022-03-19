from rest_framework import serializers
from .models import BookInventory


class BookInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInventory # this is the model that is being serialized
        fields = ( 'book_number', 'count')