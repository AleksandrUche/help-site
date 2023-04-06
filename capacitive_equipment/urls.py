from django.urls import path
from .views import *

urlpatterns = [
    path('base/', CalcCapacitiveEquipmentView.as_view(), name='base_calc_capac'),  # base page
    path('add-name-calc-capacitive/', AddCalcNameCapacitiveEquipmentView.as_view(), name='add_name_calc_capac'),
    path('all-name-calc-capacitive/', AllCalcNameCapacitiveEquipmentView.as_view(), name='all_name_calc_capac'),
    path('update-name-calc-capacitive/<int:pk>/', UpdateCalcNameCapacitiveEquipmentView.as_view(),
         name='update_name_calc_capac'),
    path('detail-name-calc-capacitive/<int:pk>/', DetailCalcNameCapacitiveEquipmentView.as_view(),
         name='detail_name_calc_capac'),
]
