from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Board, Column, Task
from .serializers import BoardSerializer, ColumnSerializer, TaskSerializer
from teams.models import Team

class BoardListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        team_id = self.request.query_params.get("team_id")
        return Board.objects.filter(team_id=team_id)

    def perform_create(self, serializer):
        team_id = self.request.data.get("team_id")
        serializer.save(
            team_id=team_id,
            created_by=self.request.user
        )


class ColumnCreateView(generics.CreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
