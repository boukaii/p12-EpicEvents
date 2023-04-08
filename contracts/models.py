from django.db import models
from django.db.models.deletion import RESTRICT
from django.conf import settings
from clients.models import Client


class Contract(models.Model):

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=RESTRICT,
                                      related_name="contract_assigned_to",
                                      blank=True,
                                      null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.CharField(max_length=50)
    payment_due = models.DateTimeField()
