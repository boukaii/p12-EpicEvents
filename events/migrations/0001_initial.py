# Generated by Django 4.1.7 on 2023-04-17 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('participants', models.IntegerField(default=0)),
                ('event_date', models.DateTimeField()),
                ('notes', models.TextField(max_length=500)),
                ('ended', models.BooleanField(default=False)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='contracts.contract')),
                ('support_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='event_assigned_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
