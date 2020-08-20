from django.http import HttpRequest, HttpResponse
from django.template import loader

def short_url(request: HttpRequest):
    template = loader.get_template('url.html')
    return HttpResponse(template.render({}))
