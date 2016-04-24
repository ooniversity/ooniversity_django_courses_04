#coding: utf-8 
from django import forms


class QuadraticForm(forms.Form):
    """ форма ввода коэффиц квадратного уравнения """
    a = forms.IntegerField(label = 'коэффициент a', required=True)
    b = forms.IntegerField(label = 'коэффициент b', required=True)
    c = forms.IntegerField(label = 'коэффициент c', required=True)

    def clean_a(self):
        """ валидация коэф 'а' на равенство 0 """
        data = self.cleaned_data['a']
        if int(data)==0:
            # добавляю сообщение об ошибке для поля 'a'
            self.add_error('a',u'коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return data