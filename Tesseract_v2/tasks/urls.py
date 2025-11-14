from django.urls import path
from .views import BoardListCreateView, ColumnCreateView, TaskCreateView

urlpatterns = [
    path('boards/', BoardListCreateView.as_view()),
    path('columns/', ColumnCreateView.as_view()),
    path('tasks/', TaskCreateView.as_view()),
]
