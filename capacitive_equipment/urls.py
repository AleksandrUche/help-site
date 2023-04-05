from django.urls import path
from .views import *

urlpatterns = [
    path('base/', CalcCapacitiveEquipmentView.as_view(), name='base_calc_capac'),
    path('add/', AddCalcCapacitiveEquipmentView.as_view(), name='add_calc_capac'),
    path('all/', AllCalcCapacitiveEquipmentView.as_view(), name='all_calc_capac'),
    path('update/<int:pk>/', UpdateCalcCapacitiveEquipmentView.as_view(), name='update_calc_capac'),
    path('detail/<int:pk>/', DetailCalcCapacitiveEquipmentView.as_view(), name='detail_calc_view'),
]
