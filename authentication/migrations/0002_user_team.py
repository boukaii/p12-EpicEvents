# Generated by Django 4.1.7 on 2023-04-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.CharField(blank=True, choices=[('Management', 'Gestion'), ('Support', 'Support'), ('Sale', 'Vente')], max_length=40),
        ),
    ]
