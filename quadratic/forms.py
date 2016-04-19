# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a')
    b = forms.IntegerField(label='коэффициент b')
    c = forms.IntegerField(label='коэффициент c')

    def clean_a(self):
        cleaned_data = super(QuadraticForm, self).clean()
        a = cleaned_data.get("a")
        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
