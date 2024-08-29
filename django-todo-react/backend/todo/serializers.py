from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import Group, User


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class TodoByID(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


