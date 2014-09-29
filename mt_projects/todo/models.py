from django.db import models
from django.contrib.auth.models import User
from mt_projects.project.models import Project

# Create your models here.
class Todo(models.Model):
    last_edited = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    text = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, blank=False)
    project = models.ForeignKey(Project, blank=True, null=True)

    def __unicode__(self):
        return self.title + ' - ' + str(self.last_edited)
