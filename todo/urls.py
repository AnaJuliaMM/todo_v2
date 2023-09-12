from django.urls import path
from todo.views.category.category import CategoryView
from todo.views.category.categoryDetail import CategoryDetailView
from todo.views.category_task.categoryTask import CategoryTaskView
from todo.views.task.task import TaskView
from todo.views.task.taskDetail import TaskDetailView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('categories/<int:pk>/tasks/', CategoryTaskView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]
