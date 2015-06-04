from django.conf.urls import *
from django.views.generic.base import TemplateView

from condottieri_help.views import HelpTemplateView

urlpatterns = patterns('condottieri_help.views',
    url(r'^$', HelpTemplateView.as_view(), name='help-index'),
    url(r'^contribute$', TemplateView.as_view(template_name='condottieri_help/contribute.html'), name='help-contribute'),
)

