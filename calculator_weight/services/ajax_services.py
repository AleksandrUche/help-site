from django.http import JsonResponse

from calculator_weight.services.services import load_class_db


def get_form_values_channel(request):
    """Выдает из БД имена швеллеров для заполнения поля формы "name"
    на основе заполненного поля "type" (AJAX)"""
    type_channel = request.GET.get('type')
    objects_channel = load_class_db(type_channel)
    channel_name_option = list(objects_channel.objects.values_list('name', flat=True))

    return JsonResponse({'channel_name_option': channel_name_option}, status=200)
