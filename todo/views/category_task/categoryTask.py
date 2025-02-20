from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.models.task import TaskEntity
from todo.models.category import CategoryEntity
from todo.serializers.task.task import TaskSerializer


class CategoryTaskView(APIView):
    """
    List all tasks for a given category.
    """
    def get(self, request, pk, format=None):
        tasks = TaskEntity.objects.filter(category_id = pk)
        serialize = TaskSerializer(tasks, many=True)
        return Response(serialize.data)
    
