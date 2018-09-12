from django.db import models
from django.contrib.auth import get_user_model

from rest_framework.reverse import reverse

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=120)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model): # add event image field
    creator     = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=120)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tags        = models.ManyToManyField(Tag)
    description = models.TextField()
    event_date  = models.DateTimeField()
    location    = models.CharField(max_length=120)
    latitude    = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude   = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_on  = models.DateTimeField(auto_now_add=True)
    attendees   = models.ManyToManyField(User, through='Attendee', related_name='attendees')

    def __str__(self):
        return self.title
    
    def get_api_uri(self, request=None):
        return reverse('api-event:detail', kwargs={"id": self.id}, request=request)

    @property
    def owner(self):
        return self.user


class AttendeeManager(models.Manager):
    def is_registered(self, event, user):
        registered = False
        qs = self.get_queryset().filter(event=event, user=user)
        if qs.exists():
            registered = True
        return registered

class Attendee(models.Model):
    event           = models.ForeignKey(Event, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_on   = models.DateTimeField(auto_now_add=True)

    objects = AttendeeManager()

    def __str__(self):
        return self.user.username
    
    def get_api_uri(self, request=None):
        return 'holla'