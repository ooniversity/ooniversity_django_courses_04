from django.db import models

class Parametr(models.Model):
    param_a = models.CharField(max_length=200)
    param_b = models.CharField(max_length=200)
    param_c = models.CharField(max_length=200)
    #def __unicode__(self):          
     #   return self.param_a

class Solution(models.Model):
    discr = models.CharField(max_length=200)
    root1 = models.CharField(max_length=200)
    root2 = models.CharField(max_length=200)
    #def __unicode__(self):          
     #   return self.param_a

class TypeParametr(models.Model):
    char_a = models.CharField(max_length=200)
    char_b = models.CharField(max_length=200)
    char_c = models.CharField(max_length=200)
    #def __unicode__(self):          
     #   return self.param_a
