from rest_framework import serializers
from todo.models.category import CategoryEntity
from todo.models.task import TaskEntity

class TaskSerializer(serializers.ModelSerializer):
   """
      Class that serialize a python object into a JSON structure  
   """
   category = serializers.SlugRelatedField(slug_field="name", read_only=True)
   
   class Meta:
        model = TaskEntity
        fields = '__all__'
     #    fields = ['id', 'name', 'category', 'description', 'percent', 'state']