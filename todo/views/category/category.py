from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.models.category import CategoryEntity 
from todo.serializers.category.category import CategorySerializer 

#Vantagens do API
    # Definir formato de exibição JSON ou tela interface


class CategoryView(APIView):
    """
    List all categories, or create a new category.
    """
    def get(self, request, format=None):
        """
            Receive a GET request and  select all records in the table Category
        """
        categories = CategoryEntity.objects.all() # O QUE eu vou manipular
        serialized_objects = CategorySerializer(categories, many=True) # COMO eu vou retornar
        return Response(serialized_objects.data)
        

    def post(self, request, format=None):
        """
            Receive a POST request and  create a new record in the table Category
        """
        #  Criando um JSON com o conteúdo do resquest de forma mais automatizada
        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        