from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.models.task import TaskEntity
from todo.serializers.task.task import TaskSerializer
from todo.serializers.task.taskPartial import TaskNameSerializer


class TaskDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, pk):
        """
            Receives a primary key and  returns an object by its primary key 
        """
        try:
            return TaskEntity.objects.get(pk=pk)
        except:
            raise Http404

        

    def get(self, request, pk, format=None):
        """
            Receives a primary key and  returns a JSON of the objects that contans the primary key in the urls  
        """
        task = self.get_object(pk)
        serializer = TaskSerializer(task) 
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
            Receives a primary key and update the fields of its objects
        """
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, pk, format=None):
        """
            Receives a primary key and update only the description field 
        """
        category = self.get_object(pk)
        serializer = TaskNameSerializer(category, data=request.data, partial = True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        """
            Receives a primary key and  delete its object  
        """
        task = self.get_object(pk)
        task.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    