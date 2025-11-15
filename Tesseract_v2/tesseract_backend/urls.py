from django.contrib import admin
from django.urls import path, include
from chat.views import ChatRoomDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/teams/', include('teams.urls')),
    path('api/chat/<int:pk>/', ChatRoomDetailView.as_view()),

]
