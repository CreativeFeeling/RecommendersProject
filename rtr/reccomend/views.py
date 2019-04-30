from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ClothingItem, Event
from .forms import TailorForm


def index(request):
    return HttpResponse("Hello!")

def tailorTag(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TailorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TailorForm()

    return render(request, 'reccomend/tailorTag.html', {'form': form})

def explore(request):
    clothing_itmes = ClothingItem.objects.order_by('-avg_rating')
    events_list = Event.objects.order_by('event_name')
    context = {
        'clothing_itmes': clothing_itmes,
        'events_list': events_list,
    }
    return render(request, 'reccomend/explore.html', context)

def event(request, event_type):
    clothing_itmes = ClothingItem.objects.order_by('-avg_rating')
    events_list = Event.objects.order_by('event_name')
    context = {
        'clothing_itmes': clothing_itmes,
        'events_list': events_list,
        'event_type': event_type,
    }
    return render(request, 'reccomend/event.html', context)
