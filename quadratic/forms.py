# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label="коэффициент a")
    b = forms.FloatField(label="коэффициент b")
    c = forms.FloatField(label="коэффициент c")

    def clean_a(self):
        if 0 in self.cleaned_data['a']:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
