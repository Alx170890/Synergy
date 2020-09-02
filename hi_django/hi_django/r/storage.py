from django.http import Http404
from shortcuts.models import *

class ShortUrlStorage(object):
    def __init__(self):
        self._short_urls = {}

    def shortcut(self, url):
        shorts = self.next()
        self._short_urls[shorts] = url
        return shorts

    def url(self, short_key, x):
        u = self._short_urls.get(short_key, None)
        shortcut = ShortUrl.objects.get(key=short_key)
        shortcut.visits += 1
        shortcut.save()
        if u is None:
            raise Http404(f'Key {short_key} not found')
        return u

    def next(self):
        num = ShortUrl.objects.count() + 1
        # num = len(self._short_urls) + 1
        return f'{num:x}'

short_storage = ShortUrlStorage()