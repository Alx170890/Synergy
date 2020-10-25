from django.http import HttpRequest, HttpResponse
from shortcuts.r.form import ShortUrlForm
from django import shortcuts

def index(request: HttpRequest):
    context = {'short_url_form': ShortUrlForm()}
    return shortcuts.render(request, 'index.html', context)
