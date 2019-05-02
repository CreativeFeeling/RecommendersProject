from django.urls import path

from . import views
from .views import tailorTag, explore

urlpatterns = [
    # ex: /reccomend
    path('', views.index, name='index'),
    # ex: /reccomend/tailor/
    path('tailor/', tailorTag.as_view(), name='tailor'),
    # ex: /reccomend/explore
    path('explore/', explore.as_view(), name='explore'),
    # ex: /reccomend/wedding
    path('<str:event_type>/', views.event, name='event'),
]
