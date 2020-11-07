from django.contrib import admin
from . import models
# Register your models here.


class SocialGroupMemberInLine(admin.TabularInline):
    model = models.SocialGroupMembers


admin.site.register(models.SocialGroup)
