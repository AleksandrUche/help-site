from django.urls import path
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
    path('metal-sheet/', SheetView.as_view(), name='sheet'),
    # Расчет массы труб
    path('tube/', TubeView.as_view(), name='tube'),
    # Расчет массы профильной трубы
    path('profile-pipe/', ProfilePipeView.as_view(), name='profile_pipe'),
    # Расчет массы швеллера
    path('channel/', СhannelView.as_view(), name='channel'),
    # Расчет массы двутавра
    path('beam/', BeamView.as_view(), name='beam'),
]
