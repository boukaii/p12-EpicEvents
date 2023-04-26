from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TEAM_ROLE = [
        ('Management', 'Gestion'),
        ('SUPPORT', 'Support'),
        ('Sale', 'Vente')
    ]
    team = models.CharField(max_length=40, choices=TEAM_ROLE, blank=True)

    def save(self, *args, **kwargs):

        if self.TEAM_ROLE == 'MANAGEMENT':
            self.is_admin = True

        return super(User, self).save(*args, **kwargs)
