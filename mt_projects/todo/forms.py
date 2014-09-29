# coding=utf8
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker
from mt_projects.todo.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('deadline', 'title', 'text', 'user')
        labels = {
            'deadline': _('Frist'),
            'title': _('Navn'),
            'text': _('Beskrivelse'),
            'user': _('Ansvarlig'),
        }
        widgets = {
            'deadline': DateTimePicker(
                options={'format': 'YYYY-MM-DD HH:mm', 'pickSeconds': False}
            ),
        }
        error_messages = {
            'title': {
                'max_length': _('Max 200 tegn.'),
            },
            'text': {
                'max_length': _('Max 200 tegn.'),
            },
            'user': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
            'title': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
        }

class TodoFormWithProject(ModelForm):
    class Meta:
        model = Todo
        fields = ('deadline', 'project', 'title', 'text', 'user')
        labels = {
            'deadline': _('Frist'),
            'project': _('Prosjekt'),
            'title': _('Navn'),
            'text': _('Beskrivelse'),
            'user': _('Ansvarlig'),
        }
        widgets = {
            'deadline': DateTimePicker(
                options={'format': 'YYYY-MM-DD HH:mm', 'pickSeconds': False}
            ),
        }
        error_messages = {
            'title': {
                'max_length': _('Max 200 tegn.'),
            },
            'text': {
                'max_length': _('Max 200 tegn.'),
            },
            'user': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
            'title': {
                'required': _(u'Dette feltet er påkrevd.'),
            },
        }
