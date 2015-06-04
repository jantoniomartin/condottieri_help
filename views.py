from django.conf import settings
from django.views.generic.base import TemplateView

class HelpTemplateView(TemplateView):
    template_name = 'condottieri_help/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HelpTemplateView, self).get_context_data(**kwargs)
        ctx.update({
            'contact_email': getattr(settings, 'CONTACT_EMAIL', ''),
            'forum_url': '/forum',
        })
        return ctx

