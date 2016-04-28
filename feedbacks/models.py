from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=255)
	subject = models.CharField(max_length=1000)
	message = models.CharField(max_length=4000)
	from_email = models.EmailField()
	create_date = models.DateTimeField(auto_now=True)
