from django.urls import path
from .views import *

urlpatterns = [
    path('', CalcCapacitiveEquipmentView.as_view(), name='base_calc_capac'),  # base page
    path('all-name-calc-capacitive/', AllCalcNameCapacitiveEquipmentView.as_view(),
         name='all_name_calc_capac'),
    # Инициализация обсчета
    path('add-name-calc-capacitive/', AddCalcNameCapacitiveEquipmentView.as_view(),
         name='add_name_calc_capac'),
    path('update-name-calc/<int:pk>/', UpdateCalcNameCapacitiveEquipmentView.as_view(),
         name='update_name_calc_capac'),
    path('detail-name-calc/<int:pk>/', DetailCalcNameCapacitiveEquipmentView.as_view(),
         name='detail_name_calc_capac'),
    # Параметры обсчетов
    path('add-parameter-calc/<int:pk>/', AddCalcParameterCapacitiveEquipmentView.as_view(),
         name='add_parameter_calc_capac'),
    path('update-parameter-calc/<int:pk>/', UpdateCalcParameterCapacitiveEquipmentView.as_view(),
         name='update_parameter_calc_capac'),
    path('detail-parameter-calc/<int:slug>/', DetailCalcParameterCapacitiveEquipmentView.as_view(),
         name='detail_parameter_calc_capac'),
]
