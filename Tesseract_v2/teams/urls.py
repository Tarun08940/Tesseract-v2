from django.urls import path
from .views import TeamListCreateView

urlpatterns = [
    path('', TeamListCreateView.as_view()),
]
