from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from events.serializers import EventSerializers
from events.models import Event
from events.permissions import IsEventFinish, IsSupportEmployeeOrReadOnly, IsSaleEmployeeConnectedToTheEventOrReadOnly


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated, IsSupportEmployeeOrReadOnly,
                          IsSaleEmployeeConnectedToTheEventOrReadOnly, IsEventFinish]
