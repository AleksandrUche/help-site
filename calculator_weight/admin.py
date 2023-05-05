from django.contrib import admin

from .models import *


@admin.register(ChannelTypeY)
class AdminChannelTypeY(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ChannelTypeP)
class AdminChannelTypeP(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ChannelTypeE)
class AdminChannelTypeE(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ChannelTypeL)
class AdminChannelTypeL(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ChannelTypeC)
class AdminChannelTypeC(admin.ModelAdmin):
    list_display = ['name']
