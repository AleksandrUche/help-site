import importlib
from django.http import JsonResponse


def load_class_db(name_cls):
    module_path = 'calculator_weight.models'
    module = importlib.import_module(module_path)
    my_class = getattr(module, name_cls)
    return my_class


def get_form_values_channel(request):
    """Выдает из БД имена швеллеров для заполнения поля формы "name"
    на основе заполненного поля "type" (AJAX)"""
    type_channel = request.GET.get('type')
    objects_channel = load_class_db(type_channel)
    channel_name_option = list(objects_channel.objects.values_list('name', flat=True))

    return JsonResponse({'channel_name_option': channel_name_option}, status=200)
