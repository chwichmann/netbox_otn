from django.contrib import admin
from .models import OMS, OCH, ChannelGroup, Channel


@admin.register(OMS)
class CommunityAdmin(admin.ModelAdmin):
    fields = ('name', 'channelgroup', 'comments')

@admin.register(OCH)
class CommunityAdmin(admin.ModelAdmin):
    fields = ('name', 'oms', 'channel', 'payload')

@admin.register(ChannelGroup)
class CommunityAdmin(admin.ModelAdmin):
    fields = ('name', 'channels', 'comments')

@admin.register(Channel)
class CommunityAdmin(admin.ModelAdmin):
    fields = ('name', 'frequency', 'wavelength')