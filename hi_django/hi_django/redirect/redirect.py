from django.http import HttpRequest, HttpResponse
def short_url(request: HttpRequest):
    return HttpResponse('url')