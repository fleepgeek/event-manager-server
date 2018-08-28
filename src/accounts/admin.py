from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'display_name', 'about',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',),
        }),
    )

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)