#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django import forms
import math

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label = "коэффициент a")
    b = forms.IntegerField(label = "коэффициент b")
    c = forms.IntegerField(label = "коэффициент c")
    def clean_a(self):
        data = super(QuadraticForm, self).clean().get('a')
        if data == 0:
            self.add_error("a", "коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return data

