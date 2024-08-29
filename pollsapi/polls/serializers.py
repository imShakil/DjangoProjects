from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Poll, Choice, Vote
from django.contrib.auth.models import User, Group, GroupManager, UserManager


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_Kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        user = User (
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollsSerilizer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

