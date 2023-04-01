from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, FormView, CreateView

from capacitive_equipment.forms import *


class CalcCapacitiveEquipmentView(LoginRequiredMixin, TemplateView):
    """Начальная страница обсчетов"""

    template_name = 'capacitive_equipment/base_calc_capacitive.html'
    extra_context = {'title': 'Обсчеты'}


class AddCalcCapacitiveEquipmentView(LoginRequiredMixin, CreateView):
    template_name = 'capacitive_equipment/add_calc_capacitive.html'
    form_class = AddPostForm
    success_url = reverse_lazy('all_calc_capac')


# class DetailCalcCapacitiveEquipmentView(LoginRequiredMixin, View):
#     template_name = 'capacitive_equipment/ .html'
#     form_class =

# class UpdateCalcCapacitiveEquipmentView(LoginRequiredMixin, ListView):
#     template_name = 'capacitive_equipment/ .html'
#     form_class =

class AllCalcCapacitiveEquipmentView(LoginRequiredMixin, ListView):
    template_name = 'capacitive_equipment/all_calc_capacitive.html'
    model = NameCapacitiveEquipment


