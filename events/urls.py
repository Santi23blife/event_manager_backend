from .views import EventView
from django.urls import path

urlpatterns = [
    path('createEvent/', EventView.as_view(), name='createEvent'),
]