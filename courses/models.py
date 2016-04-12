from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
	short_description = models.CharField(max_length=100)    
	description = models.TextField()

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
	subject = models.CharField(max_length=255)
	description = models.TextField()
	course = models.ForeignKey(Course)
    order = models.PositiveIntegerField(min_value=0, max_value=100)
	
	blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.subject
