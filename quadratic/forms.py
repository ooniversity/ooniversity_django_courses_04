# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(label="coefficient a")
    b = forms.FloatField(label="coefficient b")
    c = forms.FloatField(label="coefficient c")

    def clean_a(self):
        data = self.cleaned_data['a']
        msg = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        if data == 0:
            raise forms.ValidationError(msg)
        return data