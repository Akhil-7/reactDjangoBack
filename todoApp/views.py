from urllib import response
from django.shortcuts import render
from html5lib import serialize
from rest_framework.response import Response
from . models import Todo
from . serializers import TodoSerializers
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from todoApp import serializers
# Create your views here.


@api_view(['GET'])  
def getTodo(request):
    todo = Todo.objects.all().order_by("-id")
    serializer = TodoSerializers(todo, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def readTodo(request):
    data = request.data
    note = Todo.objects.create(
        todo=data['body']
    )
    serializer = TodoSerializers(note, many=False)
    return Response(serializer.data)
