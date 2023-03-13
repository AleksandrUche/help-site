from django import template

register = template.Library()

"""
Возвращает verbose_name для поля.
"""


@register.filter()
def get_verbose_field_name(object, field_name):
    return object._meta.get_field(field_name).verbose_name

# @register.simple_tag
# def get_verbose_field_name(object):
#     return object._meta.verbose_name

# """Вернет название таблицы из __Meta__ {{ object_name|verbose_name }}"""
# @register.filter
# def verbose_name(obj):
#     return obj._meta.verbose_name