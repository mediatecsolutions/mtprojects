from django.db import models
from mt_projects.client.models import Client
from mt_projects.project.models import Project


# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=200, blank=False)
    project = models.ForeignKey(Project, blank=True, null=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    QUOTE = 'QUOTE'
    INVOICE = 'INVOICE'
    STATUS_CHOICES = (
        (QUOTE, 'Forslag'),
        (INVOICE, 'Faktura'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=QUOTE
    )
    def __unicode__(self):
        if self.project:
            return self.project__unicode__()
        else:
            return self.name

class QuoteLine(models.Model):
    quote = models.ForeignKey(Quote, blank=False)
    text = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
