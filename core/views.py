from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home(request):
    return render(request, 'web/index.html')


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
