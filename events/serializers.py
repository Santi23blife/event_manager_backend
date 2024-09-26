from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'place', 'date', 'date_creation', 'user', 'activated_notification']
        read_only_fields = ['user', 'date_creation']
