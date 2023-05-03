from django.contrib import admin

from .models import *


@admin.register(TypeEquipment)
class AdminTypeEquipment(admin.ModelAdmin):
    list_display = ['name']


@admin.register(NameCapacitiveEquipment)
class AdminNameCapacitiveEquipment(admin.ModelAdmin):
    list_display = ['calc_number']


@admin.register(Parameter)
class AdminParameter(admin.ModelAdmin):
    list_display = ['calculation_object_id']