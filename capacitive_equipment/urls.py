from django.urls import path
from .views import *

urlpatterns = [
    path('all-view/', AllCalcCapacitiveEquipmentView.as_view(), name='all_calc_view'),
    path('detail/', DetailCalcCapacitiveEquipmentView.as_view(), name='detail_calc_view'),
    path('add/', AddCalcCapacitiveEquipmentView.as_view(), name='add_calc_capacitive'),
]
