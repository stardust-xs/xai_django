from .models import MonitoredApps
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
  return render(request=request,
                template_name='home.html',
                context={'apps': MonitoredApps.objects.all})