from rest_framework import serializers
from todo.models.category import CategoryEntity
from todo.models.task import TaskEntity

class TaskSerializer(serializers.ModelSerializer):

   class Meta:
        model = TaskEntity
        fields = '__all__'
     #    fields = ['id', 'name', 'category', 'description', 'percent', 'state']