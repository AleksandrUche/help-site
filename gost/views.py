from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .dataclasses import (
    Gost28759Request,
    Gost33259Request,
    Atk261813Request,
    Gost6533Request,
    Atk24200FlangeStoppersRequest,
    Atk26185FlangeStoppersRequest,
)
from .forms import *
from gost.handlers.atk24200_flange_stoppers_handler import Atk24200FlangeStoppersHandler
from gost.handlers.atk261813_handler import Atk261813Handler
from gost.handlers.atk26185_flange_stoppers_handler import Atk26185FlangeStoppersHandler
from gost.handlers.gost28759_handler import Gost28759Handler
from gost.handlers.gost33259_handler import Gost33259Handler
from gost.handlers.gost6533_handler import Gost6533Handler


class DocumentsView(TemplateView):
    """Начальная страница стандартов"""
    template_name = 'gost/documents.html'
    extra_context = {'title': 'Стандарты'}


class Gost33259View(View):
    """Представление для фланцев ГОСТ 33259-2015"""
    template_name = 'gost/gost_33259_flange.html'
    form_class = Gost33259Form

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={'form': form})

        handler = Gost33259Handler(Gost33259Request(**form.cleaned_data))

        return render(
            request,
            self.template_name,
            context={
                'form': self.form_class,
                'form_data': form,
                'flange_data': handler.flange_data,
                'drawing_flange_type': handler.drawing_flange_type,
                'drawing_flange_surface': handler.drawing_flange_surface,
                'fields_surface': handler.fields_surface_flange,
                'fields_type': handler.fields_type_flange,
                'surface_data': handler.surface_data,
                'mass_flange': handler.mass_flange,
            },
        )


class Gost28759View(View):
    """Представление для фланцев ГОСТ 28759.3—2022"""
    template_name = 'gost/gost_28759_flange.html'
    form_class = Gost28759Form

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={'form': form})

        handler = Gost28759Handler(Gost28759Request(**form.cleaned_data))

        return render(
            request,
            self.template_name,
            context={
                'form': self.form_class,
                'form_data': form,
                'flange_data': handler.flange_data,
                'drawing_flange_execution': handler.drawing_flange_execution,
                'mass_flange': handler.mass_flange,
                'fields_exec': handler.fields_exec,
            }
        )


class Atk261813View(View):
    """Представление для фланцев АТК 26-18-13-96"""
    template_name = 'gost/atk261813.html'
    form_class = Atk261813Form

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={'form': form})

        handler = Atk261813Handler(Atk261813Request(**form.cleaned_data))

        return render(
            request, self.template_name,
            context={
                'form': self.form_class,
                'form_data': form,
                'fields_exec': handler.fields_execution,
                'flange_data': handler.flange_data,
                'drawing_flange_execution': handler.drawing_flange_execution,
            }
        )


class Gost6533View(View):
    """Представление для днищ по ГОСТ 6533-78"""
    template_name = 'gost/gost_6533_bottom.html'
    form_class = Gost6533Form

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={'form': form})

        handler = Gost6533Handler(Gost6533Request(**form.cleaned_data))

        return render(
            request,
            self.template_name,
            context={
                'form': self.form_class,
                'form_data': form,
                'field_values': handler.field_values,
                'bottom_data': handler.bottom_data,
                'drawing_bottom': handler.drawing_bottom,
            }
        )


class Atk24200FlangeStoppersView(View):
    """Представление для заглушек АТК 24.200.02-90 (обычные)"""
    template_name = 'gost/atk24200FlangeStoppers.html'
    form_class = Atk24200FlangeStoppersForm

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={'form': form})

        handler = Atk24200FlangeStoppersHandler(Atk24200FlangeStoppersRequest(**form.cleaned_data))

        return render(
            request,
            self.template_name,
            context={
                'form': self.form_class,
                'form_data': form,
                'fields_exec': handler.fields_execution,
                'flange_data': handler.flange_data,
                'drawing_flange_execution': handler.drawing_flange_execution,
            }
        )


class Atk26185FlangeStoppersView(View):
    """Представление для заглушек АТК 26-18-5-93 (поворотные)"""
    template_name = 'gost/atk2618FlangeStoppers.html'
    form_class = Atk26185FlangeStoppersForm

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, context={'form': form})

        handler = Atk26185FlangeStoppersHandler(Atk26185FlangeStoppersRequest(**form.cleaned_data))

        return render(
            request,
            self.template_name,
            context={
                'form': self.form_class,
                'form_data': form,
                'fields_exec': handler.fields_execution,
                'flange_data': handler.flange_data,
                'drawing_flange_execution': handler.drawing_flange_execution,
            }
        )
