from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tailorTag(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def explore(request):
    response = "You're looking at reccomendations based on just your sizes"
    return HttpResponse(response)

def event(request, event_type):
    return HttpResponse("You're looking at reccomendations for %s." % event_type)
