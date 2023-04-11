from rest_framework import serializers
from events.models import Event


class EventSerializers(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = ['id', 'name', 'contract', 'date_created', 'date_updated', 'support_contact',
                  'event_date', 'attendees', 'event_date', 'notes']
