import pytest
from shortcuts.models import ShortUrl


@pytest.fixture()
def short_key(url):
    # print(url)
    short = ShortUrl(url=url, key=hash(url))
    short.save()
    assert short


@pytest.mark.django_db
def test_long(client, short_key):
    response = client.get(f'/r/{short_key.key}')
    assert response.status_code == 302
    assert response.url == short_key.url