#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django import forms
import math

class QuadraticForm(forms.Form):
    a = forms.FloatField(label = "коэффициент a")
    b = forms.FloatField(label = "коэффициент b")
    c = forms.FloatField(label = "коэффициент c")
    def clean(self):
        data = super(QuadraticForm, self).clean()
        if data.get('a') == 0:
            self.add_error("a", "коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return data

