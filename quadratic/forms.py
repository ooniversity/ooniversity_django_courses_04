# -*- coding: UTF-8 -*-
from django import forms
# from quadratic.models import Quadratic


class QuadraticForm(forms.Form):
    # class Meta:
        # model = Quadratic
    a = forms.IntegerField(label="coefficient a", initial="")
    b = forms.IntegerField(label="coefficient b", initial="")
    c = forms.IntegerField(label="coefficient c", initial="")

    def clean_a(self):
        if self.cleaned_data['a'] == 0:
            raise forms.ValidationError(u"коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return self.cleaned_data['a']
