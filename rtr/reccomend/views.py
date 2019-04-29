from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ClothingItem, Event


def index(request):
    return HttpResponse("Hello!")

def tailorTag(request):
    return HttpResponse("Enter in your sizes:")

def explore(request):
    response = "You're looking at reccomendations based on just your sizes"
    return HttpResponse(response)

def event(request, event_type):
    clothing_itmes = ClothingItem.objects.order_by('-avg_rating')
    events_list = Event.objects.order_by('event_name')
    context = {
        'clothing_itmes': clothing_itmes,
        'events_list': events_list,
        'event_type': event_type,
    }
    return render(request, 'reccomend/event.html', context)
    return HttpResponse("You're looking at reccomendations for %s." % event_type)
