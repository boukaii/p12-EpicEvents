from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TEAM_ROLE = [
        ('Management', 'Gestion'),
        ('Support', 'Support'),
        ('Sale', 'Vente')
    ]
    team = models.CharField(max_length=40, choices=TEAM_ROLE, blank=True)

    def save(self, *args, **kwargs):

        if self.TEAM_ROLE == 'MANAGEMENT':
            self.is_admin = True

        if self.password is not None:
            self.set_password(self.password)
        return super(User, self).save(*args, **kwargs)

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name']
    #     )
    #
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     return user
