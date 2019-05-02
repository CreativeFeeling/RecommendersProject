from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse

from .models import ClothingItem, Event
from .forms import TailorForm

import numpy as np
import pandas as pd

class tailorTag(FormView):

    form_class = TailorForm
    template_name = 'reccomend/tailorTag.html'
    success_url = reverse_lazy('explore')

    def form_valid(self, form):

        # if this is a POST request we need to process the form data
        if self.request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = TailorForm(self.request.POST)
            # check whether it's valid:
            if form.is_valid():
                # set session variables
                self.request.session['size'] = form.get_size()
                self.request.session['bust'] = form.get_bust()
                self.request.session['clothing_type'] = form.get_clothing_type()
                self.request.session['occasion'] = form.get_occasion()
                return HttpResponseRedirect(self.success_url)

        # if a GET (or any other method) we'll create a blank form
        else:
            form = TailorForm()

        return super(tailorTag, self).form_valid(form)

def index(request):
    return HttpResponse("Hello!")

# class explore
class explore(TemplateView):
    template_name = 'reccomend/explore.html'

    def item_list(self):
        rentTheRunway = pd.read_csv("/Users/marcoortiztorres/Desktop/data.csv")
        category = self.request.session.get('clothing_type')
        bust = self.request.session.get('bust')
        size = self.request.session.get('size')
        occasion = self.request.session.get('occasion')

        if category:
            category_match = rentTheRunway.loc[rentTheRunway["category"] == category]
        else: category_match = rentTheRunway
        if bust:
            bust_match = category_match.loc[category_match["bust size"] == bust]
        else: bust_match = category_match

        if size:
            size_match = bust_match.loc[bust_match["size"] == size]
        else: size_match = bust_match

        if occasion:
            occasion_match = size_match.loc[size_match["rented for"] == occasion]
        else: occasion_match = size_match

        return_matches = occasion_match.loc[occasion_match["rating"] >= 6]
        items = return_matches.groupby('item_id').agg({"rating" : 'mean', "item_id" : 'first', "rented for" : 'first', "image" : "first"})

        item_ids = items["item_id"].tolist()
        ratings = items["rating"].tolist()
        urls = items["image"].tolist()
        data = items.to_json()

        return(item_ids, ratings, urls)

    def get_context_data(self):
        ids, ratings, urls = self.item_list()
        scoptywoop = zip(ids, ratings, urls)
        events_list = Event.objects.order_by('event_name')
        context = {
            'scoptywoop': scoptywoop,
            'events_list': events_list,
        }
        return context

def item_list(category, bust, size, occasion):
    rentTheRunway = pd.read_csv("/Users/marcoortiztorres/Desktop/data.csv")

    if category:
        category_match = rentTheRunway.loc[rentTheRunway["category"] == category]
    else: category_match = rentTheRunway
    if bust:
        bust_match = category_match.loc[category_match["bust size"] == bust]
    else: bust_match = category_match

    if size:
        size_match = bust_match.loc[bust_match["size"] == size]
    else: size_match = bust_match

    if occasion:
        occasion_match = size_match.loc[size_match["rented for"] == occasion]
    else: occasion_match = size_match

    return_matches = occasion_match.loc[occasion_match["rating"] >= 6]
    items = return_matches.groupby('item_id').agg({"rating" : 'mean', "item_id" : 'first', "rented for" : 'first', "image" : "first"})

    item_ids = items["item_id"].tolist()
    ratings = items["rating"].tolist()
    urls = items["image"].tolist()
    data = items.to_json()

    return(item_ids, ratings, urls)

def event(request, event_type):
    category = request.session.get('clothing_type')
    bust = request.session.get('bust')
    size = request.session.get('size')
    ids, ratings, urls = item_list(category, bust, size, event_type)
    scoptywoop = zip(ids, ratings, urls)
    clothing_itmes = ClothingItem.objects.order_by('-avg_rating')
    events_list = Event.objects.order_by('event_name')
    context = {
        'scoptywoop': scoptywoop,
        'events_list': events_list,
        'event_type': event_type,
    }
    return render(request, 'reccomend/event.html', context)
