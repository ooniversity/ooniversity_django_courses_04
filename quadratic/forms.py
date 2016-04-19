#coding: utf-8 
from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(label = 'коэффициент a', required=False,max_length=10)
    b = forms.CharField(label = 'коэффициент b', required=False,max_length=10)
    c = forms.CharField(label = 'коэффициент c', required=False,max_length=10)


    def clean_a(self):
        data = self.cleaned_data['a']
        if  data.replace('.','').replace('-','').isdigit() and int(data)==0:
            self.add_error('a',u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
            #raise forms.ValidationError(u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return data

    def clean(self):
        koef=[0]*3
        koef_names=('a','b','c')
        cleaned_data = super(QuadraticForm, self).clean()
        for i in range(0,3):
            koef[i]=cleaned_data.get(koef_names[i])        
            if  koef[i]==None or koef[i]=='':                
                self.add_error(koef_names[i],u'This field is required.')
            elif  not koef[i].replace('.','').replace('-','').isdigit(): 
                self.add_error(koef_names[i],u'коэффициент не целое число')

