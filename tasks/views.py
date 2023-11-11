from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskAPIView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
