from django.contrib import admin
from .models import SocialGroup, SocialGroupMembers
# Register your models here.


class SocialGroupMemberInLine(admin.TabularInline):
    model = SocialGroupMembers


admin.site.register(SocialGroup)
