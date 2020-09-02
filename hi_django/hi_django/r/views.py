from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from hi_django.form import ShortUrlForm
from django import shortcuts
from .storage import short_storage
import random
import string

from shortcuts.models import *

def short_url(request: HttpRequest):
    rend = str(''.join(random.choice(string.ascii_letters) for x in range(7)))
    if request.method != "POST":
        return HttpResponse(status=405)
    short_url_form = ShortUrlForm(request.POST)
    context = {'short_url_form': short_url_form}
    if not short_url_form.is_valid():
        return shortcuts.render(request, 'index.html', context)
    url = short_url_form.cleaned_data['url']
    short_key = short_storage.shortcut(url)
    short_rend_key = str(short_key + rend)
    scheme = request.scheme
    host = request.get_host()
    port = request.get_port()
    port = '' if port not in {80, 443} else f':{port}'
    cont = {'short_url': f'{scheme}://{host}{port}/r/{short_rend_key}'}
    ShortUrl(url=url, short=cont.get('short_url'), key=short_key).save()
    return shortcuts.render(request, 'url.html', cont)

def long_url(request: HttpRequest, short_key):
    short_keys = short_key[:-7]
    url = short_storage.url(short_keys, short_key)
    return HttpResponseRedirect(url)