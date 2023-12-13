from django.urls import path
from .views import *
from .services.ajax_services import (
    get_form_values_gost_33259,
    get_form_values_atk_261813,
    get_form_values_gost_28759,
    get_form_values_atk_24200_flange_stoppers,
    get_form_values_atk_26185_flange_stoppers,
    get_form_values_gost_6533,
)

urlpatterns = [
    path('', DocumentsView.as_view(), name='documents'),  # начальная страница документов
    path('gost-33259-2015/', Gost33259View.as_view(), name='gost33259'),  # Фланцы ГОСТ 33259-2017
    path('atk-26-18-13-96/', Atk261813View.as_view(), name='atk261813'),  # Фланцы АТК 26-18-14-98
    path('gost-28759-3-2022/', Gost28759View.as_view(), name='gost28759'),  # Фланцы ГОСТ 28759.3—2022
    path('atk-24-200-02-90/', Atk24200FlangeStoppersView.as_view(), name='atk24200'),  # заглушки АТК
    path('atk-26-18-5-93/', Atk26185FlangeStoppersView.as_view(), name='atk26185'),  # заглушки АТК поворотные
    path('gost-6533-78/', Gost6533View.as_view(), name='gost6533'),  # днища
]

ajax_urls = [
    path('gost-33259-2015/get-values-form/', get_form_values_gost_33259, name='get_values_gost_33259'),
    path('atk-26-18-13-96/get-values-form/', get_form_values_atk_261813, name='get_values_atk_261813'),
    path('gost-28759-3-2022/get-values-form/', get_form_values_gost_28759, name='get_values_gost_28759'),
    path('atk-24-200-02-90/get-values-form/',
         get_form_values_atk_24200_flange_stoppers,
         name='get_values_atk_24200_flange_stoppers'
         ),
    path('atk-26-18-5-93/get-values-form/',
         get_form_values_atk_26185_flange_stoppers,
         name='get_values_atk_26185_flange_stoppers'
         ),
    path('gost-6533-78/get-values-form/', get_form_values_gost_6533, name='get_values_gost_6533'),
]

urlpatterns.extend(ajax_urls)
