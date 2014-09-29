# coding=utf8
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker
from mt_projects.project.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'brief', 'client', 'responsible', 'start_time', 'end_time')
        labels = {
            'name': _('Navn'),
            'client': _('Kunde'),
            'responsible': _('Deltagere'),
            'start_time': _('Start'),
            'end_time': _('Slutt'),
        }
        help_texts = {
            'responsible': _(u'Hold nede Ctrl (Cmd på mac) for å velge mer enn en.'),
        }
        error_messages = {
            'name': {
                'max_length': _('Max 200 tegn.'),
                'required': _(u'Dette feltet er påkrevd.'),
            },
            'text': {
                'max_length': _('Max 200 tegn.'),
            },
            'start_time': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
            'end_time': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
            'responsible': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
        }
        widgets = {
            'start_time': DateTimePicker(
                options={'format': 'YYYY-MM-DD HH:mm', 'pickSeconds': False}
            ),
            'end_time': DateTimePicker(
                options={'format': 'YYYY-MM-DD HH:mm', 'pickSeconds': False}
            )
        }
