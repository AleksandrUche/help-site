import importlib
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import *
from .models import *
import math
from decimal import Decimal


class CalculatorWeighView(TemplateView):
    """Страница отображения всех калькуляторов"""
    template_name = 'calculator_weight/all_calculator_weight.html'
    extra_context = {'title': 'Металлопрокат'}


"""Металлопрокат"""


class CornerEqualShelvesView(View):
    template_name = 'calculator_weight/corner_equal_shelves.html'
    form_class = CornerEqualShelvesWeightForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                side = form.cleaned_data['side']
                thickness = form.cleaned_data['thickness']
                length = form.cleaned_data['length']
                material = form.cleaned_data['material']

                # Расчет массы уголка
                calculation_weight = \
                    (side / 1000 * 2 - thickness / 1000) * thickness / 1000 * length / 1000 * Decimal(material)
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))
                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class CornerDifferentShelvesView(View):
    template_name = 'calculator_weight/corner_different_shelves.html'
    form_class = CornerDifferentShelvesWeightForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                side = form.cleaned_data['side']
                side_b = form.cleaned_data['side_b']
                thickness = form.cleaned_data['thickness']
                length = form.cleaned_data['length']
                material = form.cleaned_data['material']

                # Расчет массы уголка не равнополочного
                calculation_weight = \
                    (side / 1000 + side_b / 1000 - thickness / 1000) * thickness / 1000 * length / 1000 * Decimal(
                        material)
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))

                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class CircleView(View):
    template_name = 'calculator_weight/circle.html'
    form_class = CircleForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                diameter = form.cleaned_data['diameter']
                length = form.cleaned_data['length']
                material = form.cleaned_data['material']

                # Расчет массы круга
                calculation_weight = Decimal(math.pi) / 4 * Decimal(material) * (diameter / 1000) ** 2 * length / 1000
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))

                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class SquareView(View):
    template_name = 'calculator_weight/square.html'
    form_class = SquareForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                size = form.cleaned_data['size']
                length = form.cleaned_data['length']
                material = form.cleaned_data['material']

                # Расчет массы квадрата
                calculation_weight = Decimal(material) * (size / 1000) ** 2 * length / 1000
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))

                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class SheetView(View):
    template_name = 'calculator_weight/sheet.html'
    form_class = SheetForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                side_a = form.cleaned_data['side_a']
                side_b = form.cleaned_data['side_b']
                thickness = form.cleaned_data['thickness']
                material = form.cleaned_data['material']

                # Расчет массы листа
                calculation_weight = side_a / 1000 * side_b / 1000 * thickness / 1000 * Decimal(material)
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))

                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class TubeView(View):
    template_name = 'calculator_weight/tube.html'
    form_class = TubeForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                diameter = form.cleaned_data['diameter']
                thickness = form.cleaned_data['thickness']
                length = form.cleaned_data['length']
                material = form.cleaned_data['material']
                # Внутренний диаметр
                inner_diameter = diameter / 1000 - 2 * thickness / 1000
                # Площадь
                square = Decimal(math.pi) / 4 * ((diameter / 1000) ** 2 - inner_diameter ** 2)
                # Расчет массы листа
                calculation_weight = square * length / 1000 * Decimal(material)
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))

                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class ProfilePipeView(View):
    template_name = 'calculator_weight/profile_pipe.html'
    form_class = ProfileTubeForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                side_a = form.cleaned_data['side_a']
                side_b = form.cleaned_data['side_b']
                thickness = form.cleaned_data['thickness']
                length = form.cleaned_data['length']
                material = form.cleaned_data['material']

                # Расчет массы профильной трубы
                calculation_weight = (Decimal(material) / Decimal('7850') * Decimal('0.0157') * thickness * (
                        side_a + side_b - Decimal('2.86') * thickness)) * length / 1000
                # Округление до двух знаков после запятой
                rounded_weight = calculation_weight.quantize(Decimal('1.000'))

                return JsonResponse({'weight': rounded_weight}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


def load_class_db(name_cls):
    module_path = 'calculator_weight.models'
    module = importlib.import_module(module_path)
    my_class = getattr(module, name_cls)
    return my_class


class ChannelView(View):
    template_name = 'calculator_weight/channel.html'
    form_class = ChannelForm

    def get(self, request):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.form_class(request.GET)

            if form.is_valid():
                type_channel = form.cleaned_data['type']
                name = form.cleaned_data['name']
                length = form.cleaned_data['length']

                objects_channel = load_class_db(type_channel)
                weight_channel = objects_channel.objects.get(name=name)
                calculation_weight = Decimal(weight_channel.weight) * length / 1000
                rounded_weight = calculation_weight.quantize(Decimal('1.0'))

                return JsonResponse({'weight': rounded_weight,
                                     'type': type_channel,
                                     'values': {'height': weight_channel.height,
                                                'width': weight_channel.width,
                                                'thickness': weight_channel.thickness,
                                                'thickness_t': weight_channel.thickness_t,
                                                }
                                     },
                                    status=200
                                    )

        return render(request, self.template_name, context={'form': self.form_class})


def get_form_values_channel(request):
    type_channel = request.GET.get('type')
    objects_channel = load_class_db(type_channel)
    channel_name_option = list(objects_channel.objects.values_list('name', flat=True))

    return JsonResponse({'channel_name_option': channel_name_option}, status=200)


class BeamView(View):
    # template_name = 'calculator_weight/beam.html'
    # form_class = BeamForm
    pass
