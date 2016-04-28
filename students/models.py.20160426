from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    courses = models.ManyToManyField('courses.Course')

    def __unicode__(self):
        return self.surname

    def my_property(self):
        return u'{} {}'.format(self.name, self.surname)

    my_property.short_description = 'Full name'
    full_name = property(my_property)




    
