from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from capacitive_equipment.forms import *


class CalcCapacitiveEquipmentView(LoginRequiredMixin, TemplateView):
    """Начальная страница обсчетов"""
    template_name = 'capacitive_equipment/base_calc_capacitive.html'
    extra_context = {'title': 'Обсчеты'}


class AllCalcCapacitiveEquipmentView(LoginRequiredMixin, ListView):
    """Все обсчеты"""
    template_name = 'capacitive_equipment/all_calc_capacitive.html'
    model = NameCapacitiveEquipment


class AddCalcCapacitiveEquipmentView(LoginRequiredMixin, CreateView):
    """Добавление обсчета"""
    template_name = 'capacitive_equipment/add_calc_capacitive.html'
    form_class = AddCapacEquipmentForm
    # success_url = reverse_lazy('all_calc_capac')


class DetailCalcCapacitiveEquipmentView(LoginRequiredMixin, DetailView):
    """Просмотр определенного обсчета"""
    model = NameCapacitiveEquipment
    fields = ['name_equipment', 'type_equipment', 'calc_number', 'author', 'created_date']
    template_name = 'capacitive_equipment/detail_calc_capacitive.html'


class UpdateCalcCapacitiveEquipmentView(LoginRequiredMixin, UpdateView):
    """Редактирование обсчета"""
    model = NameCapacitiveEquipment
    fields = ['name_equipment', 'type_equipment', 'calc_number', 'author']
    template_name = 'capacitive_equipment/update_calc_capacitive.html'
    success_url = reverse_lazy('all_calc_capac')
