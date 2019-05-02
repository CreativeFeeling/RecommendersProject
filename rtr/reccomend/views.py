from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse

from .models import ClothingItem, Event
from .forms import TailorForm

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
                self.request.session['age'] = form.get_age()
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
    def get_context_data(self):
        clothing_itmes = ClothingItem.objects.order_by('-avg_rating')
        events_list = Event.objects.order_by('event_name')
        age = self.request.session.get('age')
        context = {
            'age': age,
            'clothing_itmes': clothing_itmes,
            'events_list': events_list,
        }
        return context

def event(request, event_type):
    clothing_itmes = ClothingItem.objects.order_by('-avg_rating')
    events_list = Event.objects.order_by('event_name')
    context = {
        'clothing_itmes': clothing_itmes,
        'events_list': events_list,
        'event_type': event_type,
    }
    return render(request, 'reccomend/event.html', context)
