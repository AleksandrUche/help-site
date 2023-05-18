from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views import View

from .forms import *
from .models import *
from django.shortcuts import render
import importlib


def load_class_db(name_cls):
    module_path = 'gost.models'
    module = importlib.import_module(module_path)
    my_class = getattr(module, name_cls)
    return my_class


class DocumentsView(TemplateView):
    template_name = 'gost/documents.html'
    extra_context = {'title': 'Стандарты'}


# Отображение поиска фланцев по ГОСТ 33259-2015
class Gost33259View(View):
    template_name = 'gost/gost33259.html'
    form_class = Gost33259Form

    def get(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
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

        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        # Значения которые нужно вывести при выборе ряда 1 и ряда 2 (уплотнительная поверхность)
        values_surface_fl = {
            1: {
                'B': ['h_lower', 'd2'],
                'C': ['h1_lower', 'd3_row_one', 'd4_row_one'],
                'D': ['h_lower', 'h2_lower', 'd2', 'd6_row_one', 'd5_row_one'],
                'E': ['h1_lower', 'd4_row_one'],
                'F': ['h_lower', 'h2_lower', 'd2', 'd6_row_one'],
            },
            2: {
                'B': ['h_lower', 'd2'],
                'C': ['h1_lower', 'd3_row_two', 'd4_row_two'],
                'D': ['h_lower', 'h2_lower', 'd2', 'd6_row_two', 'd5_row_two'],
                'E': ['h1_lower', 'd4_row_two'],
                'F': ['h_lower', 'h2_lower', 'd2', 'd6_row_two'],
            }
        }

        if form.is_valid():
            type_fl = form.cleaned_data['type_fl']
            surface_fl = form.cleaned_data['surface']
            dn_passage = form.cleaned_data['dn_passage']
            pn = form.cleaned_data['pn']
            row = form.cleaned_data['row']

            objects_types_fl = load_class_db(f'Gost33259Type{type_fl}')

            drawing_flange_type = Gost33259TypeDrawing.objects.filter(type_fl=type_fl)
            drawing_flange_surface = Gost33259SurfaceDrawing.objects.filter(surface_fl=surface_fl)
            flange_data = objects_types_fl.objects.filter(dn_passage=dn_passage, pn=pn)
            surface_data = Gost33259SurfaceValues.objects.filter(dn_passage=dn_passage, pn=pn)
            if pn != '250':  # в ГОСТ есть давление 250, но массы на них нет
                if pn == '2.5':
                    pn = '2'
                mass_flange = Gost33259Mass.objects.filter(dn_passage=dn_passage,
                                                           type_fl=type_fl).values_list(f'pn_{pn}', flat=True).get()
            else:
                mass_flange = None
            # необходимые поля из БД для отображения в шаблоне
            fields_surface = values_surface_fl[row][surface_fl]

            # Gost33259Type01  ['dn_passage', 'pn', 'dv_lower_row_one', 'dv_lower_row_two', 'b_lower_row_one', 'b_lower_row_two',
            # 'c1_lower', 'd_row_one', 'd_row_two', 'd1', 'd_lower_row_one', 'd_lower_row_two', 'n_lower_row_one',
            # 'n_lower_row_two', 'pin_row_one', 'pin_row_two']

            # Gost33259Type02['dn_passage', 'pn', 'd0_row_one', 'd0_row_two', 'd2', 'dv_lower_row_one', 'dv_lower_row_two',
            #  'b_lower_row_one', 'b_lower_row_two', 'b1_lower_row_one', 'b1_lower_row_two', 'c_lower_row_one',
            #  'c_lower_row_two', 'c1_lower', 'd_row_one', 'd_row_two', 'd1', 'd_lower_row_one', 'd_lower_row_two',
            #  'n_lower_row_one', 'n_lower_row_two', 'pin_row_one', 'pin_row_two']

            # Gost33259Type11
            # ['dn_passage', 'pn', 'dm_row_one', 'dm_row_two', 'dn_row_one', 'dn_row_two', 'd1_lower_row_one',
            #  'd1_lower_row_two', 'b_lower_row_one', 'b_lower_row_two', 'h_row_one', 'h_row_two', 'h1', 'd_row_one',
            #  'd_row_two', 'd1', 'd_lower_row_one', 'd_lower_row_two', 'n_lower_row_one', 'n_lower_row_two',
            #  'pin_row_one', 'pin_row_two']
            fields_type = [field.name for field in objects_types_fl._meta.get_fields()][1:]

            return render(request, self.template_name,
                          context={'form': form,
                                   'flange_data': flange_data,
                                   'drawing_flange_type': drawing_flange_type,
                                   'drawing_flange_surface': drawing_flange_surface,
                                   'fields_surface': fields_surface,
                                   'fields_type': fields_type,
                                   'surface_data': surface_data,
                                   'mass_flange': mass_flange,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})


'''Отображение поиска фланцев по АТК 26-18-13-96'''


class Atk261813View(View):
    template_name = 'gost/atk261813.html'
    form_class = Atk261813Form

    def get(self, request):
        form = self.form_class

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            execution = request.GET.get('execution')
            pn = request.GET.get('pn')
            objects_exec_fl = load_class_db(f'Atk261813FlangeExec{execution}')

            if execution and not pn:
                pn_option = list(objects_exec_fl.objects.values_list('pn', flat=True).distinct())
                return JsonResponse({'pn_option': pn_option}, status=200)

            if execution and pn:
                dn_passage_option = list(objects_exec_fl.objects.filter(pn=pn).values_list('dn_passage', flat=True))
                return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)

        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            execution = form.cleaned_data['execution']
            pn = form.cleaned_data['pn']
            dn_passage = form.cleaned_data['dn_passage']

            objects_exec_fl = load_class_db(f'Atk261813FlangeExec{execution}')

            flange_data = objects_exec_fl.objects.filter(dn_passage=dn_passage, pn=pn)
            drawing_flange_execution = Atk261813FlangeDrawing.objects.filter(execution_fl=execution)
            fields_exec = [field.name for field in objects_exec_fl._meta.get_fields()][1:]
            return render(request, self.template_name,
                          context={'form': form,
                                   'fields_exec': fields_exec,
                                   'flange_data': flange_data,
                                   'drawing_flange_execution': drawing_flange_execution,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})


'''Отображение поиска Днищ по ГОСТ 6533-78'''


class Gost6533View(View):
    template_name = 'gost/gost6533.html'
    form_class = Gost6533Form

    def get(self, request):
        form = self.form_class

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            drawing = request.GET.get('drawing')
            diameter = request.GET.get('diameter')

            if drawing and not diameter:
                diameter_option = list(
                    Gost6533Bottoms.objects.filter(exec=drawing).values_list('d', flat=True).order_by('d').distinct())
                return JsonResponse({'diameter_option': diameter_option}, status=200)

            if drawing and diameter:
                thickness_option = list(Gost6533Bottoms.objects.filter(d=diameter).values_list('s_lower', flat=True))
                return JsonResponse({'thickness_option': thickness_option}, status=200)

        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            diameter = form.cleaned_data['diameter']
            drawing = form.cleaned_data['drawing']
            thickness = form.cleaned_data['thickness']

            field_values = [field.name for field in Gost6533Bottoms._meta.get_fields()][2:]
            bottom_data = Gost6533Bottoms.objects.filter(exec=drawing, d=diameter, s_lower=thickness)
            drawing_bottom = Gost6533BottomsDrawing.objects.filter(execution=drawing)
            return render(request, self.template_name,
                          context={'form': form,
                                   'field_values': field_values,
                                   'bottom_data': bottom_data,
                                   'drawing_bottom': drawing_bottom,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})


'''Заглушки АТК 24.200.02-90 (обычные)'''


class Atk24200FlangeStoppersView(View):
    template_name = 'gost/atk24200FlangeStoppers.html'
    form_class = Atk24200FlangeStoppersForm

    def get(self, request):
        form = self.form_class

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            execution = request.GET.get('execution')
            pn = request.GET.get('pn')
            objects_exec_fl = load_class_db(f'Atk24200FlangeStoppersExec{execution}')

            if execution and not pn:
                pn_option = list(objects_exec_fl.objects.values_list('pn', flat=True).distinct())
                return JsonResponse({'pn_option': pn_option}, status=200)

            if execution and pn:
                dn_passage_option = list(objects_exec_fl.objects.filter(pn=pn).values_list('dn_passage', flat=True))
                return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)

        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            execution = form.cleaned_data['execution']
            pn = form.cleaned_data['pn']
            dn_passage = form.cleaned_data['dn_passage']

            objects_exec_fl = load_class_db(f'Atk24200FlangeStoppersExec{execution}')

            flange_data = objects_exec_fl.objects.filter(dn_passage=dn_passage, pn=pn)
            drawing_flange_execution = Atk24200FlangeStoppersDrawing.objects.filter(execution_fl=execution)
            fields_exec = [field.name for field in objects_exec_fl._meta.get_fields()][1:]
            return render(request, self.template_name,
                          context={'form': form,
                                   'fields_exec': fields_exec,
                                   'flange_data': flange_data,
                                   'drawing_flange_execution': drawing_flange_execution,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})


'''Заглушки ПОВОРОТНЫЕ АТК 26-18-5-93'''


class Atk26185FlangeStoppersView(View):
    template_name = 'gost/atk2618FlangeStoppers.html'
    form_class = Atk26185FlangeStoppersForm

    def get(self, request):
        form = self.form_class

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            execution = request.GET.get('execution')
            pn = request.GET.get('pn')
            objects_exec_fl = load_class_db(f'Atk2618FlangeStoppersExec{execution}')

            if execution and not pn:
                pn_option = list(objects_exec_fl.objects.values_list('pn', flat=True).distinct())
                return JsonResponse({'pn_option': pn_option}, status=200)

            if execution and pn:
                dn_passage_option = list(objects_exec_fl.objects.filter(pn=pn).values_list('dn_passage', flat=True))
                return JsonResponse({'dn_passage_option': dn_passage_option}, status=200)

        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            execution = form.cleaned_data['execution']
            pn = form.cleaned_data['pn']
            dn_passage = form.cleaned_data['dn_passage']

            objects_exec_fl = load_class_db(f'Atk2618FlangeStoppersExec{execution}')

            flange_data = objects_exec_fl.objects.filter(dn_passage=dn_passage, pn=pn)
            drawing_flange_execution = Atk2618FlangeStoppersDrawing.objects.filter(execution_fl=execution)
            fields_exec = [field.name for field in objects_exec_fl._meta.get_fields()][1:]
            return render(request, self.template_name,
                          context={'form': form,
                                   'fields_exec': fields_exec,
                                   'flange_data': flange_data,
                                   'drawing_flange_execution': drawing_flange_execution,
                                   }
                          )
        return render(request, self.template_name, context={'form': form})
