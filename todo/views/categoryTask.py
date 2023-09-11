from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryTaskView(APIView):
    """
    List all tasks for a given category.
    """
    def get(self, request, pk, format=None):
        pass
    
