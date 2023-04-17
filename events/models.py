from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.conf import settings
from contracts.models import Contract


class Event(models.Model):
    name = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract,
                                 on_delete=CASCADE,
                                 related_name="test",
                                 null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=RESTRICT,
                                        related_name="event_assigned_to",
                                        null=True)

    participants = models.IntegerField(default=0)
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=500)
    cloturer = models.BooleanField(default=False)
