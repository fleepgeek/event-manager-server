from django.contrib import admin

from .models import Event, Tag, Category

class EventAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title',)

admin.site.register(Event, EventAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)