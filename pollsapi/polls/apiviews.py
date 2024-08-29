from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from .models import Poll, Choice, User
from .serializers import PollsSerilizer, ChoiceSerializer, VoteSerializer, UserSerializer

class PollList(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    print(queryset)
    serializer_class = PollsSerilizer

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        print(request.user)
        print(poll.created_by)
        if not request.user == poll.created_by:
            raise PermissionDenied("You can't delete this poll")
        return super().destroy(request, *args, **kwargs)

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollsSerilizer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id = self.kwargs["pk"])
        return queryset
    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        print(request.user)
        print(poll.created_by)
        if not request.user == poll.created_by:
            raise PermissionDenied("You can't create choice for this poll.")
        return super().post(request, *args, **kwargs)

    #queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {
            'choice': choice_pk, 'poll': pk, 'voted_by': voted_by
        }
        print(voted_by)
        print(data)
        serializer = VoteSerializer(data=data)
        print(serializer)
        if serializer is not None and serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class Loginview(APIView):
    permission_classes = ()
    def post(self, request, ):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({
                "error": "Wrong credentials! Please try again."
            },
            status=status.HTTP_400_BAD_REQUEST
            )
