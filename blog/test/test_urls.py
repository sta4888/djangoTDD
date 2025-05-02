from blog.urls import blog
import pytest
from django.urls import reverse, resolve
from blog.views import post

@pytest.mark.django_db
class TestBlogURLs:
    """Тесты URL"""

    def test_homepage_url_name(self, client):
        response = client.get(reverse('blog:post_list'))
        assert response.status_code == 200

    def test_root_url_resolves_to_homepage_view(self):
        """Проверка, что URL /blog/ разрешается к представлению blog"""
        found = resolve('/blog/')  # Убедись, что это правильный путь
        assert found.func == blog  # Здесь должно быть представление для /blog/


    def test_post_url_name(self, client, catalog_instance):
        """Тест для URL страницы поста с id из фикстуры"""
        url = reverse('blog:post', kwargs={'id': catalog_instance.id})  # Пример с id из фикстуры
        response = client.get(url)

        # Проверка успешности запроса
        assert response.status_code == 200

    def test_post_url_resolves_to_post_view(self, catalog_instance):
        """Проверка разрешения URL для страницы поста"""
        found = resolve(f'/blog/post/{catalog_instance.id}')
        assert found.func == post

