import pytest
from shortcuts.models import ShortUrl


@pytest.mark.django_db
def test_short(client, url):
    request = client.post('/r/', data={'url': url})
    assert request.status_code == 200
    assert ShortUrl.objects.count() == 1
    assert ShortUrl.objects.get(url=url) is not None

@pytest.mark.django_db
def test_short_get_not_allowed(client):
    request = client.get('/r/')
    assert request.status_code == 405