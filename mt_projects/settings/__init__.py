from mt_projects.settings.base import *

try:
    from mt_projects.settings.local import *
except ImportError:
    raise ImportError('Failed to import local settings')
