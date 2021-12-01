"""Configuration of the admin interface for clubs."""
from django.contrib import admin
from .models import User, Membership, Club, Tournament

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""

    list_display = [
        'id','username', 'name', 'email'
    ]

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = [
        'id','club', 'user'
    ]

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'owner'
    ]

@admin.register(Tournament)
class TorunamentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'organizer'
    ]
