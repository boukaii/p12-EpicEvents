from rest_framework import viewsets
from events.serializers import EventSerializers
from events.models import Event


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializers
    