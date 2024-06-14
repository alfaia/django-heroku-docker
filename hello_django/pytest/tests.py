# test_home_page.py (nome do arquivo sugerido para seguir a convenção pytest)

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

def test_home_page_status_code(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

def test_home_page_template(client):
    url = reverse('home')
    response = client.get(url)
    assertTemplateUsed(response, 'home.html')

