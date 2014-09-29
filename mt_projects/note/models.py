from django.db import models
from django.contrib.auth.models import User
from mt_projects.project.models import Project


class Note(models.Model):
    last_edited = models.DateTimeField(auto_now=True, auto_now_add=True)
    text = models.CharField(max_length=1000, blank=False)
    user = models.ForeignKey(User, blank=False)
    project = models.ForeignKey(Project, blank=True, null=True)

    def __unicode__(self):
        return self.text[0:25]
