from django.contrib import admin
from .models import *


@admin.register(Gost33259AvailabilityFlange)
class AdminGost33259AvailabilityFlange(admin.ModelAdmin):
    """Применяемость фланцев"""
    list_display = [field.name for field in Gost33259AvailabilityFlange._meta.get_fields()]


@admin.register(Gost33259Type01)
class AdminGost33259Type01(admin.ModelAdmin):
    """Размеры фланцев тип 01 ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259Type01._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259Type02)
class AdminGost33259Type02(admin.ModelAdmin):
    """Размеры фланцев тип 02 ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259Type02._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259Type11)
class AdminGost33259Type11(admin.ModelAdmin):
    """Размеры фланцев тип 11 ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259Type11._meta.get_fields()]
    list_filter = ('dn_passage',)


@admin.register(Gost33259SurfaceValues)
class AdminGost33259SurfaceValues(admin.ModelAdmin):
    """Размеры уплотнительных поверхностей фланцев ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259SurfaceValues._meta.get_fields()]
    empty_value_display = 'пусто'


@admin.register(Gost33259Mass)
class AdminGost33259Mass(admin.ModelAdmin):
    """Массы фланцев по ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259Mass._meta.get_fields()]


@admin.register(Gost33259TypeDrawing)
class AdminGost33259TypeDrawing(admin.ModelAdmin):
    """Чертежи типов фланцев по ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259TypeDrawing._meta.get_fields()]


@admin.register(Gost33259SurfaceDrawing)
class AdminGost33259SurfaceDrawing(admin.ModelAdmin):
    """Чертежи уплотнительных поверхностей для фланцев по ГОСТ 33259-2017"""
    list_display = [field.name for field in Gost33259SurfaceDrawing._meta.get_fields()]


@admin.register(Atk261813FlangeExec1)
class AdminAtk261813FlangeExec1(admin.ModelAdmin):
    """Размеры фланцев по АТК 26-18-14-98 (Исполнение 1)"""
    list_display = [field.name for field in Atk261813FlangeExec1._meta.get_fields()]


@admin.register(Atk261813FlangeExec2)
class AdminAtk261813FlangeExec2(admin.ModelAdmin):
    """Размеры фланцев по АТК 26-18-14-98 (Исполнение 2)"""
    list_display = [field.name for field in Atk261813FlangeExec2._meta.get_fields()]


@admin.register(Atk261813FlangeExec3)
class AdminAtk261813FlangeExec3(admin.ModelAdmin):
    """Размеры фланцев по АТК 26-18-14-98 (Исполнение 3)"""
    list_display = [field.name for field in Atk261813FlangeExec3._meta.get_fields()]


@admin.register(Atk261813FlangeExec4)
class AdminAtk261813FlangeExec4(admin.ModelAdmin):
    """Размеры фланцев по АТК 26-18-14-98 (Исполнение 4)"""
    list_display = [field.name for field in Atk261813FlangeExec4._meta.get_fields()]


@admin.register(Atk261813FlangeExec5)
class AdminAtk261813FlangeExec5(admin.ModelAdmin):
    """Размеры фланцев по АТК 26-18-14-98 (Исполнение 5)"""
    list_display = [field.name for field in Atk261813FlangeExec5._meta.get_fields()]


@admin.register(Atk261813FlangeExec6)
class AdminAtk261813FlangeExec6(admin.ModelAdmin):
    """Размеры фланцев по АТК 26-18-14-98 (Исполнение 6)"""
    list_display = [field.name for field in Atk261813FlangeExec6._meta.get_fields()]


@admin.register(Atk261813FlangeDrawing)
class AdminAtk261813FlangeDrawing(admin.ModelAdmin):
    """Чертежи фланцев по АТК 26-18-14-98"""
    list_display = [field.name for field in Atk261813FlangeDrawing._meta.get_fields()]


@admin.register(Gost28759FlangeValues)
class AdminGost28759FlangeValues(admin.ModelAdmin):
    """Размеры для фланцев по ГОСТ 28759.3—2022"""
    list_display = [field.name for field in Gost28759FlangeValues._meta.get_fields()]


@admin.register(Gost28759FlangeMass)
class AdminGost28759FlangeMass(admin.ModelAdmin):
    """Масса фланцев по ГОСТ 28759.3—2022"""
    list_display = [field.name for field in Gost28759FlangeMass._meta.get_fields()]


@admin.register(Gost28759FlangeDrawing)
class AdminGost28759FlangeDrawing(admin.ModelAdmin):
    """Чертежи фланцев по ГОСТ 28759.3—2022"""
    list_display = [field.name for field in Gost28759FlangeDrawing._meta.get_fields()]


@admin.register(Atk24200FlangeStoppersExec1)
class AdminAtk24200FlangeStoppersExec1(admin.ModelAdmin):
    """Размеры и массы заглушек по АТК 24.200.02-90 (Исполнение 1)"""
    list_display = [field.name for field in Atk24200FlangeStoppersExec1._meta.get_fields()]


@admin.register(Atk24200FlangeStoppersExec2)
class AdminAtk24200FlangeStoppersExec2(admin.ModelAdmin):
    """Размеры и массы заглушек по АТК 24.200.02-90 (Исполнение 2)"""
    list_display = [field.name for field in Atk24200FlangeStoppersExec2._meta.get_fields()]


@admin.register(Atk24200FlangeStoppersExec3)
class AdminAtk24200FlangeStoppersExec3(admin.ModelAdmin):
    """Размеры и массы заглушек по АТК 24.200.02-90 (Исполнение 3)"""
    list_display = [field.name for field in Atk24200FlangeStoppersExec3._meta.get_fields()]


@admin.register(Atk24200FlangeStoppersExec4)
class AdminAtk24200FlangeStoppersExec4(admin.ModelAdmin):
    """Размеры и массы заглушек по АТК 24.200.02-90 (Исполнение 4)"""
    list_display = [field.name for field in Atk24200FlangeStoppersExec4._meta.get_fields()]


@admin.register(Atk24200FlangeStoppersExec5)
class AdminAtk24200FlangeStoppersExec5(admin.ModelAdmin):
    """Размеры и массы заглушек по АТК 24.200.02-90 (Исполнение 5)"""
    list_display = [field.name for field in Atk24200FlangeStoppersExec5._meta.get_fields()]


@admin.register(Atk24200FlangeStoppersDrawing)
class AdminAtk24200FlangeStoppersDrawing(admin.ModelAdmin):
    """Чертежи заглушек по АТК 24.200.02-90"""
    list_display = [field.name for field in Atk24200FlangeStoppersDrawing._meta.get_fields()]


@admin.register(Atk2618FlangeStoppersExec1)
class AdminAtk2618FlangeStoppersExec1(admin.ModelAdmin):
    """Размеры и массы заглушек поворотных по АТК 26-18-5-93 (Исполнение 1)"""
    list_display = [field.name for field in Atk2618FlangeStoppersExec1._meta.get_fields()]


@admin.register(Atk2618FlangeStoppersExec2)
class AdminAtk2618FlangeStoppersExec2(admin.ModelAdmin):
    """Размеры и массы заглушек поворотных по АТК 26-18-5-93 (Исполнение 2)"""
    list_display = [field.name for field in Atk2618FlangeStoppersExec2._meta.get_fields()]


@admin.register(Atk2618FlangeStoppersExec3)
class AdminAtk2618FlangeStoppersExec3(admin.ModelAdmin):
    """Размеры и массы заглушек поворотных по АТК 26-18-5-93 (Исполнение 3)"""
    list_display = [field.name for field in Atk2618FlangeStoppersExec3._meta.get_fields()]


@admin.register(Atk2618FlangeStoppersDrawing)
class AdminAtk2618FlangeStoppersDrawing(admin.ModelAdmin):
    """Чертежи заглушек поворотных по АТК 26-18-5-93"""
    list_display = [field.name for field in Atk2618FlangeStoppersDrawing._meta.get_fields()]


@admin.register(Gost6533Bottoms)
class AdminGost6533Bottoms(admin.ModelAdmin):
    """Размеры и массы днищ по ГОСТ 6533-78"""
    list_display = [field.name for field in Gost6533Bottoms._meta.get_fields()]


@admin.register(Gost6533BottomsDrawing)
class AdminGost6533BottomsDrawing(admin.ModelAdmin):
    """Чертежи днищ по ГОСТ 6533-78"""
    list_display = [field.name for field in Gost6533BottomsDrawing._meta.get_fields()]
