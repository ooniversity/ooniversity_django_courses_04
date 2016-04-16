from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=200)
	short_description = models.CharField(max_length=300)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name
		
class Lesson(models.Model):
	subject = models.CharField(max_length=200)
	description = models.TextField()
	course = models.ForeignKey(Course)
	order = models.PositiveIntegerField()

	def __unicode__(self):
		return self.subject

