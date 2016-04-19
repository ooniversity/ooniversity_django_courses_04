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
            #self.add_error('a',u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
            raise forms.ValidationError(u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return data

    def clean(self):
        koef=[0]*3
        koef_names=('a','b','c')
        cleaned_data = super(QuadraticForm, self).clean()
        for i in range(0,3):
            koef[i]=cleaned_data.get(koef_names[i])        
            if  not koef[i].replace('.','').replace('-','').isdigit(): 
                self.add_error(koef_names[i],u'коэффициент не целое число')

