# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(label='Coefficient A')
    b = forms.FloatField(label='Coefficient B')
    c = forms.FloatField(label='Coefficient C')

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError('''коэффициент при первом слагаемом
                уравнения, не может быть равным нулю''')
        else:
            return data

            