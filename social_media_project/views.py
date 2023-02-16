from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'


class LoggedInPage(TemplateView):
    template_name = 'logged_in.html'


class ComeBackPage(TemplateView):
    template_name = 'come_back.html'