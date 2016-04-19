# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    """Form"""
    a = forms.IntegerField(label="коэффициент a")
    b = forms.IntegerField(label="коэффициент b")
    c = forms.IntegerField(label="коэффициент c")

    def clean_a(self):
        data = self.cleaned_data['a']
        msg = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        if data == 0:
            raise forms.ValidationError(msg)
        return data

