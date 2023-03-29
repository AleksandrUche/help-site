from django.urls import path
from .views import *

urlpatterns = [
    path('base/', CalcCapacitiveEquipmentView.as_view(), name='base_calc_capac'),
    path('add/', AddCalcCapacitiveEquipmentView.as_view(), name='add_calc_capac'),
    path('all-view/', AllCalcCapacitiveEquipmentView.as_view(), name='all_calc_capac'),
    #     path('detail/', DetailCalcCapacitiveEquipmentView.as_view(), name='detail_calc_view'),
]
