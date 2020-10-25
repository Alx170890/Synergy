import pytest


@pytest.fixture(params=['mail.yandex', 'google', 'surf.alx170890.beget'])
def domain(request):
    return request.param

@pytest.fixture(params=['http', 'https'])
def scheme(request):
    return request.param

@pytest.fixture(params=['ru', 'com', 'tech'])
def url(request, domain, scheme):
    return f'{scheme}://{request.param}.{domain}'