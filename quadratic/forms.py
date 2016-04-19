# -*- coding: UTF-8 -*-
from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a', widget=forms.TextInput) #error_messages={'required': 'коэффициент не определен', 'invalid': 'коэффициент не целое число'})
    b = forms.IntegerField(label='коэффициент b', widget=forms.TextInput)
    c = forms.IntegerField(label='коэффициент c', widget=forms.TextInput)
    
    def clean(self):
        if self.cleaned_data.get('a') == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return self.cleaned_data

