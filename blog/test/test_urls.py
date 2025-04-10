# blog/test/test_urls.py
import pytest
from django.urls import reverse, resolve
from blog.views import blog

# проверка url правильный ли вью подбирается
@pytest.mark.django_db
def test_post_list_url_resolves():
    url = reverse('blog:post_list')
    assert resolve(url).func == blog
