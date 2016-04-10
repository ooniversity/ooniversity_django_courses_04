from django.db import models

# Create your models here.
class Quadratic(models.Model):
	a = models.IntegerField(default=None)
	b = models.IntegerField(default=None)
	c = models.IntegerField(default=None)
	d = models.IntegerField(default=None)
	x1 = models.IntegerField(default=None)
	x2 = models.IntegerField(default=None)