from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookInventory
from .serializers import BookInventorySerializer


@api_view(['GET', 'POST', 'PUT'])
def bookinventory(request):
    
    if request.method == 'GET': # user requesting data 
        snippets = BookInventory.objects.all()
        serializer = BookInventorySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # user adding / posting data
        snippets = BookInventory.objects.all().filter(book_number=request.data.get("book_number"))
        snippets.delete()
        serializer = BookInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT': # user putting/updating data
        snippets = BookInventory.objects.all().filter(book_number=request.data.get("book_number"))
        snippets.delete()
        serializer = BookInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def singlebookinventory(request, queryparams):
    if request.method == 'GET': # user requesting data 
        snippets = BookInventory.objects.all().filter(book_number=queryparams)
        serializer = BookInventorySerializer(snippets, many=True)
        return Response(serializer.data)