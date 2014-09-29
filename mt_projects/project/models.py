from django.db import models
from django.contrib.auth.models import User
from mt_projects.client.models import Client
from tinymce.models import HTMLField

class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    brief = HTMLField(blank=True, null=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    responsible = models.ManyToManyField(User, related_name='project_responsible')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)

    def __unicode__(self):
        if self.client:
            return self.name + ' - ' + self.client.name
        else:
            return self.name
