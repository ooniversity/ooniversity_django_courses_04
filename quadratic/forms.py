# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(label=u"коэффициент a")
    b = forms.CharField(label=u"коэффициент b")
    c = forms.CharField(label=u"коэффициент c")

    def clean_a(self):
        data = self.cleaned_data['a']
        if int(data)==0:
            self.add_error('a',u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return data

