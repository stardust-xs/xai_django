from django.http import HttpResponse


def index(request):
  """Render index page/UI."""
  return HttpResponse('Great, This works!')