from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, response, permissions
from .serializers import TodoSerializers, TodoByID, GroupSerializer, UserSerializer
from .models import Todo


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
