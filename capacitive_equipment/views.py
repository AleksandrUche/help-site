import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from capacitive_equipment.forms import *


class CalcCapacitiveEquipmentView(LoginRequiredMixin, TemplateView):
    """Начальная страница обсчетов"""
    template_name = 'capacitive_equipment/base_calc_capacitive.html'
    extra_context = {'title': 'Обсчеты'}


class AllCalcNameCapacitiveEquipmentView(LoginRequiredMixin, ListView):
    """Все обсчеты"""
    template_name = 'capacitive_equipment/all_name_calc_capacitive.html'
    model = NameCapacitiveEquipment


class AddCalcNameCapacitiveEquipmentView(LoginRequiredMixin, CreateView):
    """Добавление обсчета"""
    template_name = 'capacitive_equipment/add_name_calc_capacitive.html'
    form_class = AddNameCapacEquipmentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailCalcNameCapacitiveEquipmentView(LoginRequiredMixin, DetailView):
    """Просмотр определенного обсчета"""
    model = NameCapacitiveEquipment
    fields = ['name_equipment', 'type_equipment', 'calc_number', 'author', 'created_date']
    template_name = 'capacitive_equipment/detail_name_calc_capacitive.html'


class UpdateCalcNameCapacitiveEquipmentView(LoginRequiredMixin, UpdateView):
    """Редактирование обсчета"""
    model = NameCapacitiveEquipment
    fields = ['name_equipment', 'type_equipment', 'calc_number']
    template_name = 'capacitive_equipment/update_name_calc_capacitive.html'
    # success_url = reverse_lazy('all_calc_capac')


class AddCalcParameterCapacitiveEquipmentView(LoginRequiredMixin, CreateView):
    """Добавление параметров аппарата емкостного"""
    template_name = 'capacitive_equipment/add_name_calc_capacitive.html'
    form_class = AddParameterCapacEquipmentForm


class DetailCalcParameterCapacitiveEquipmentView(LoginRequiredMixin, DetailView):
    """Просмотр определенного обсчета"""
    model = Parameter
    fields = '__all__'
    template_name = 'capacitive_equipment/detail_parameter_calc_capacitive.html'


class UpdateCalcParameterCapacitiveEquipmentView(LoginRequiredMixin, UpdateView):
    """Редактирование параметров обсчета"""
    model = Parameter
    fields = '__all__'
    template_name = 'capacitive_equipment/update_parameter_calc_capacitive.html'
