# Generated by Django 2.1 on 2018-09-12 10:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0004_attendee_registered_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attendees', through='event.Attendee', to=settings.AUTH_USER_MODEL),
        ),
    ]
