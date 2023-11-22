from django.urls import path

from .services import get_form_values_channel
from .views import *

urlpatterns = [
    # Калькуляторы металлопроката
    path('', CalculatorWeighView.as_view(), name='calculator_weigh'),
    # Расчет массы уголка равнополочного
    path('corner-equal/', CornerEqualShelvesView.as_view(), name='corner_equal'),
    # Расчет массы уголка разнополочного
    path('corner-different/', CornerDifferentShelvesView.as_view(), name='corner_different'),
    # Расчет массы кругляка
    path('circle/', CircleView.as_view(), name='circle'),
    # Расчет массы квадрата
    path('square/', SquareView.as_view(), name='square'),
    # Расчет массы листа
    path('sheet/', SheetView.as_view(), name='sheet'),
    # Расчет массы труб
    path('tube/', TubeView.as_view(), name='tube'),
    # Расчет массы профильной трубы
    path('profile-pipe/', ProfilePipeView.as_view(), name='profile_pipe'),
    # Расчет массы швеллера по ГОСТ
    path('channel/', ChannelView.as_view(), name='channel'),
    # Получение из БД имеющихся швеллеров для заполнения поля формы "name"
    path('channel/get-values-channel/', get_form_values_channel, name='get_values_channel'),
    # Получение из БД имеющихся двутавров для заполнения поля формы "name"
    path('channel/get-values-i-beam/', get_form_values_channel, name='get_values_beam'),
    # Расчет массы двутавра по ГОСТ
    path('i-beam/', BeamView.as_view(), name='beam'),
]
