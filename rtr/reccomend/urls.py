from django.urls import path

from . import views

urlpatterns = [
    # ex: /reccomend
    path('', views.index, name='index'),
    # ex: /reccomend/tailor/
    path('tailor/', views.tailorTag, name='tailor'),
    # ex: /reccomend/explore
    path('explore/', views.explore, name='explore'),
    # ex: /reccomend/wedding
    path('<str:event_type>/', views.event, name='event'),
]
