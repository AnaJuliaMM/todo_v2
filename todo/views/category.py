from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryView(APIView):
    """
    List all categories, or create a new category.
    """
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

