# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    """Form"""
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()

    def clean_a(self):
        data = self.cleaned_data['a']
        msg = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        if data == 0:
            raise forms.ValidationError(msg)
        return data

