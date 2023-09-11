from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskView(APIView):
    """
    List all tasks, or create a new task.
    """    
    def get_category(self, pk):
        pass
        
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass
    
