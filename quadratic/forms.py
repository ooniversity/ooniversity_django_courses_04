# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    """
    Input variables of the quadratic equation
    """
    a = forms.FloatField(label='Введите коэффициент a ', widget=forms.TextInput(attrs={'size': '10'}))
    b = forms.FloatField(label='Введите коэффициент b ', widget=forms.TextInput(attrs={'size': '10'}))
    c = forms.FloatField(label='Введите коэффициент c ', widget=forms.TextInput(attrs={'size': '10'}))

    def clean_a(self):
        """
        check the first coefficient of the quadratic equation
        """
        if int(self.cleaned_data['a']) == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        else:
            return self.cleaned_data['a']
