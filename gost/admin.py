from django.contrib import admin

from .models import *

'''Фланцы'''


@admin.register(Gost33259AvailabilityFlange)
class AdminGost33259AvailabilityFlange(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259AvailabilityFlange._meta.get_fields()]


@admin.register(Gost33259Type01)
class AdminGost33259Type01(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259Type01._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259Type02)
class AdminGost33259Type02(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259Type02._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259Type11)
class AdminGost33259Type11(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259Type11._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259SurfaceValues)
class AdminGost33259SurfaceValues(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259SurfaceValues._meta.get_fields()]
    empty_value_display = 'пусто'


@admin.register(Gost33259Mass)
class AdminGost33259Mass(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259Mass._meta.get_fields()]


@admin.register(Gost33259TypeDrawing)
class AdminGost33259TypeDrawing(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259TypeDrawing._meta.get_fields()]


@admin.register(Gost33259SurfaceDrawing)
class AdminGost33259SurfaceDrawing(admin.ModelAdmin):
    list_display = [field.name for field in Gost33259SurfaceDrawing._meta.get_fields()]


@admin.register(Atk261813FlangeExec1)
class AdminAtk261813FlangeExec1(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec1._meta.get_fields()]


@admin.register(Atk261813FlangeExec2)
class AdminAtk261813FlangeExec2(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec2._meta.get_fields()]


@admin.register(Atk261813FlangeExec3)
class AdminAtk261813FlangeExec3(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec3._meta.get_fields()]


@admin.register(Atk261813FlangeExec4)
class AdminAtk261813FlangeExec4(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec4._meta.get_fields()]


@admin.register(Atk261813FlangeExec5)
class AdminAtk261813FlangeExec5(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec5._meta.get_fields()]


@admin.register(Atk261813FlangeExec6)
class AdminAtk261813FlangeExec6(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeExec6._meta.get_fields()]


@admin.register(Atk261813FlangeDrawing)
class AdminAtk261813FlangeDrawing(admin.ModelAdmin):
    list_display = [field.name for field in Atk261813FlangeDrawing._meta.get_fields()]


'''Днища'''


@admin.register(Gost6533Bottoms)
class AdminGost6533Bottoms(admin.ModelAdmin):
    list_display = [field.name for field in Gost6533Bottoms._meta.get_fields()]


@admin.register(Gost6533BottomsDrawing)
class AdminGost6533BottomsDrawing(admin.ModelAdmin):
    list_display = [field.name for field in Gost6533BottomsDrawing._meta.get_fields()]
