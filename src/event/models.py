from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


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


class Event(models.Model):
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

    def __str__(self):
        return self.title
    
    @property
    def owner(self):
        return self.user
