from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.conf import settings
from contracts.models import Contract


# class EventStatus(models.Model):
#     status = models.CharField(max_length=25, unique=True)
#
#     class Meta:
#         # verbose_name = "Event Status"
#         verbose_name_plural = "Event Status"
#
#     def __str__(self):
#         return f"{self.status}"


class Event(models.Model):

    CHOICES_STATUS = (
        (1, 'Not attributed'),
        (2, 'Begin'),
        (3, 'In Progress'),
        (4, 'Ended')

    )
    event_status = models.PositiveSmallIntegerField(choices=CHOICES_STATUS, verbose_name="Status", default=1)
    # event_status = models.ForeignKey(EventStatus, on_delete=models.PROTECT)
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
