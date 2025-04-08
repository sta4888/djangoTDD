import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db

def test_post_list_view(client):
    # Тестируем URL для списка постов
    url = reverse('blog:post_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'No posts available' in response.content.decode()
