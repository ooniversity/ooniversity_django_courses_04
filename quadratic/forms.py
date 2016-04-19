#coding: utf-8 
from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label = 'коэффициент a', required=True)
    b = forms.IntegerField(label = 'коэффициент b', required=True)
    c = forms.IntegerField(label = 'коэффициент c', required=True)


    def clean_a(self):
        data = self.cleaned_data['a']
        #if  data.replace('.','').replace('-','').isdigit() and 
        if int(data)==0:
            self.add_error('a',u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
            #raise forms.ValidationError(u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return data


