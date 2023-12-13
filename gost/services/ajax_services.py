from django.http import JsonResponse

from gost.models import Gost28759FlangeValues, Gost6533Bottoms
from gost.services.services import load_class_db


def get_form_values_gost_33259(request):
    """Выдает из БД условный проход фланцев (dn_passage_option) и давление (pn_option)
    на основе заполненных полей "type_fl", "dn_passage" (AJAX)"""
    type_fl = request.GET.get('type_fl')
    dn_passage = request.GET.get('dn_passage')
    objects_types_fl = load_class_db(f'Gost33259Type{type_fl}')

    if type_fl and not dn_passage:
        dn_passage_option = list(
            objects_types_fl.objects.values_list('dn_passage', flat=True).order_by('dn_passage').distinct())
        return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)

    if type_fl and dn_passage:
        pn_option = list(objects_types_fl.objects.filter(dn_passage=dn_passage).values_list('pn', flat=True))
        return JsonResponse({'pn_option': pn_option}, status=200)


def get_form_values_gost_28759(request):
    """Выдает из БД давление (pn_option)
    на основе заполненного поля "dn_passage" (AJAX)"""
    dn_passage = request.GET.get('dn_passage')

    if dn_passage:
        pn_option = list(
            Gost28759FlangeValues.objects.filter(dn_passage=dn_passage).values_list('pn', flat=True)
        )
        return JsonResponse({'pn_option': pn_option}, status=200)


def get_form_values_atk_261813(request):
    """Выдает из БД условный проход фланцев (dn_passage_option) и давление (pn_option)
    на основе заполненных полей "execution", "pn" (AJAX)"""
    execution = request.GET.get('execution')
    pn = request.GET.get('pn')
    objects_exec_fl = load_class_db(f'Atk261813FlangeExec{execution}')

    if execution and not pn:
        pn_option = list(objects_exec_fl.objects.values_list('pn', flat=True).distinct())
        return JsonResponse({'pn_option': pn_option}, status=200)

    if execution and pn:
        dn_passage_option = list(objects_exec_fl.objects.filter(pn=pn).values_list('dn_passage', flat=True))
        return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)


def get_form_values_gost_6533(request):
    """Выдает из БД диаметр днищ (diameter_option) и толщину (thickness_option)
    на основе заполненных полей "drawing", "diameter" (AJAX)"""
    drawing = request.GET.get('drawing')
    diameter = request.GET.get('diameter')

    if drawing and not diameter:
        diameter_option = list(
            Gost6533Bottoms.objects.filter(exec=drawing).values_list('d', flat=True).order_by('d').distinct())
        return JsonResponse({'diameter_option': diameter_option}, status=200)

    if drawing and diameter:
        thickness_option = list(Gost6533Bottoms.objects.filter(d=diameter).values_list('s_lower', flat=True))
        return JsonResponse({'thickness_option': thickness_option}, status=200)


def get_form_values_atk_24200_flange_stoppers(request):
    """Выдает из БД условный проход заглушки (dn_passage_option) и давление (pn_option)
    на основе заполненных полей "execution", "pn" (AJAX)"""
    execution = request.GET.get('execution')
    pn = request.GET.get('pn')
    objects_exec_fl = load_class_db(f'Atk24200FlangeStoppersExec{execution}')

    if execution and not pn:
        pn_option = list(objects_exec_fl.objects.values_list('pn', flat=True).distinct())
        return JsonResponse({'pn_option': pn_option}, status=200)

    if execution and pn:
        dn_passage_option = list(objects_exec_fl.objects.filter(pn=pn).values_list('dn_passage', flat=True))
        return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)


def get_form_values_atk_26185_flange_stoppers(request):
    """Выдает из БД условный проход заглушки (поворотной) (dn_passage_option)
    и давление (pn_option) на основе заполненных полей "execution", "pn" (AJAX)"""
    execution = request.GET.get('execution')
    pn = request.GET.get('pn')
    objects_exec_fl = load_class_db(f'Atk2618FlangeStoppersExec{execution}')

    if execution and not pn:
        pn_option = list(objects_exec_fl.objects.values_list('pn', flat=True).distinct())
        return JsonResponse({'pn_option': pn_option}, status=200)

    if execution and pn:
        dn_passage_option = list(objects_exec_fl.objects.filter(pn=pn).values_list('dn_passage', flat=True))
        return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)
