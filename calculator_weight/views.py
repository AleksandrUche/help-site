from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import (
    CornerEqualShelvesWeightForm,
    CornerDifferentShelvesWeightForm,
    CircleForm,
    SquareForm,
    SheetForm,
    TubeForm,
    ProfileTubeForm,
    ChannelForm,
    BeamForm,
)

from calculator_weight.services.services import load_class_db
from calculator_weight.services.calculators_services import (
    calculate_mass_corner_equal,
    calculate_mass_corner_different,
    calculate_mass_circle,
    calculate_mass_square,
    calculate_mass_sheet,
    calculate_mass_tube,
    calculate_mass_profile_pipe,
    calculate_mass_of_reference_values,
)


class CalculatorWeightView(TemplateView):
    """Страница отображения всех калькуляторов"""
    template_name = 'calculator_weight/all_calculator_weight.html'
    extra_context = {'title': 'Металлопрокат'}


class CornerEqualShelvesView(View):
    """Уголок равнополочный"""
    template_name = 'calculator_weight/corner_equal_shelves.html'
    form_class = CornerEqualShelvesWeightForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            side = form.cleaned_data['side']
            thickness = form.cleaned_data['thickness']
            length = form.cleaned_data['length']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_corner_equal(side, thickness, length, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class CornerDifferentShelvesView(View):
    """Уголок неравнополочный"""
    template_name = 'calculator_weight/corner_different_shelves.html'
    form_class = CornerDifferentShelvesWeightForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            side = form.cleaned_data['side']
            side_b = form.cleaned_data['side_b']
            thickness = form.cleaned_data['thickness']
            length = form.cleaned_data['length']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_corner_different(side, side_b, thickness, length, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class CircleView(View):
    """Кругляк"""
    template_name = 'calculator_weight/circle.html'
    form_class = CircleForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            diameter = form.cleaned_data['diameter']
            length = form.cleaned_data['length']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_circle(diameter, length, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class SquareView(View):
    """Квадрат"""
    template_name = 'calculator_weight/square.html'
    form_class = SquareForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            size = form.cleaned_data['size']
            length = form.cleaned_data['length']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_square(size, length, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class SheetView(View):
    """Лист"""
    template_name = 'calculator_weight/sheet.html'
    form_class = SheetForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            side_a = form.cleaned_data['side_a']
            side_b = form.cleaned_data['side_b']
            thickness = form.cleaned_data['thickness']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_sheet(side_a, side_b, thickness, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class TubeView(View):
    """Трубы"""
    template_name = 'calculator_weight/tube.html'
    form_class = TubeForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            diameter = form.cleaned_data['diameter']
            thickness = form.cleaned_data['thickness']
            length = form.cleaned_data['length']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_tube(diameter, thickness, length, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class ProfilePipeView(View):
    """Профильные трубы"""
    template_name = 'calculator_weight/profile_pipe.html'
    form_class = ProfileTubeForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            side_a = form.cleaned_data['side_a']
            side_b = form.cleaned_data['side_b']
            thickness = form.cleaned_data['thickness']
            length = form.cleaned_data['length']
            material = form.cleaned_data['material']

            calculated_mass = calculate_mass_profile_pipe(side_a, side_b, thickness, length, material)

            return JsonResponse({'weight': calculated_mass}, status=200)

        return render(request, self.template_name, context={'form': self.form_class})


class ChannelView(View):
    """Швеллеры"""
    template_name = 'calculator_weight/channel.html'
    form_class = ChannelForm

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            type_channel = form.cleaned_data['type']
            name = form.cleaned_data['name']
            length = form.cleaned_data['length']

            objects_channel = load_class_db(type_channel)
            weight_channel = objects_channel.objects.get(name=name)

            calculated_mass = calculate_mass_of_reference_values(weight_channel.weight, length)

            return JsonResponse(
                {
                    'weight': calculated_mass,
                    'type': type_channel,
                    'values': {
                        'height': weight_channel.height,
                        'width': weight_channel.width,
                        'thickness': weight_channel.thickness,
                        'thickness_t': weight_channel.thickness_t,
                    }
                },
                status=200
            )

        return render(request, self.template_name, context={'form': self.form_class})


class BeamView(ChannelView):
    """Двутавры"""
    template_name = 'calculator_weight/beam.html'
    form_class = BeamForm
