from django.urls import path
from . import views
urlpatterns = [
    path('getTodo/', views.getTodo),
    path('readTodo/', views.readTodo),
]
