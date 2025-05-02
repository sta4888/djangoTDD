import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage_template(client):
    response = client.get(reverse('blog:post_list'))
    templates = [t.name for t in response.templates]
    assert 'blog/post_list.html' in templates

@pytest.mark.django_db
def test_homepage_contains_correct_html(client):
    response = client.get(reverse('blog:post_list'))
    assert 'No posts available' in response.content.decode()

@pytest.mark.django_db
def test_homepage_does_not_contain_incorrect_html(client):
    response = client.get(reverse('blog:post_list'))
    assert 'Hello World' not in response.content.decode()
