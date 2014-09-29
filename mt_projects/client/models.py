from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    mail = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name
