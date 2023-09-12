from rest_framework import serializers
from todo.models.category import CategoryEntity
from todo.serializers.task.task import TaskSerializer

class CategoryDesciptionSerializer(serializers.ModelSerializer):
    """
      Class that serialize a python object into a JSON structure  
   """

    class Meta:
        """
            Class that contains a attribute called "model" that receives the Model used in the Serializer and the attribute "fields" used to   determine the fields that will be serialized  
        """
        model = CategoryEntity
        fields = ['description']
