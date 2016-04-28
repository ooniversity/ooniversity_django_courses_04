from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=25)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    from_email = models.EmailField(verbose_name = 'Your Email')
    create_date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.from_email
