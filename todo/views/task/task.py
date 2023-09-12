from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.models.task import TaskEntity
from todo.models.category import CategoryEntity
from todo.serializers.task.task import TaskSerializer


class TaskView(APIView):
    """
    List all tasks, or create a new task.
    """    
    def get_category(self, pk):
        """
            Receives a primary key and  returns an object by its primary key 
        """
        try: 
             # GET()  retorna 1 / FILTER() retorna vários
             return CategoryEntity.objects.get(pk=pk)
        except:
            raise Http404
    
              
    def get(self, request, format=None):
        """
            Receive a GET request and  select all records in the table Category
        """
        tasks = TaskEntity.objects.all()
        serialize = TaskSerializer(tasks, many=True)
        return Response(serialize.data)

    def post(self, request, format=None):
        """
            Receives a POST request and  create a new record in the table Task
        """
        category = self.get_category(request.data.get("category"))
        serializer = TaskSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save(category=category)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


        

    
