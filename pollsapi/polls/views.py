from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
# Create your views here.
from .models import Poll, Choice, Vote


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list(polls.values("question", "created_by__username", "pub_date"))
    }
    print(data)
    print(polls)
    return JsonResponse(data)

def polls_details(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "result": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
        }
    }
    return JsonResponse(data)
