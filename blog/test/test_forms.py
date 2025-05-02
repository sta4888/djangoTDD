import pytest
from django.urls import reverse

from blog.forms import AddPostForm


@pytest.mark.django_db
def test_book_form_is_in_context_and_contains_csrf(client, catalog_instance):
    response = client.get(reverse('blog:post', kwargs={'id': catalog_instance.id}))

    # Проверка, что форма передана в контекст и правильного типа
    form = response.context.get('form')
    assert isinstance(form, AddPostForm)

    # Проверка, что в HTML-ответе есть csrf-токен
    content = response.content.decode()
    assert '<input type="hidden" name="csrfmiddlewaretoken"' in content


@pytest.mark.django_db
def test_bootstrap_class_used_for_default_styling(client, catalog_instance):
    response = client.get(reverse('blog:post', kwargs={'id': catalog_instance.id}))
    form = response.context.get('form')
    assert 'class="form-control"' in form.as_p()

def test_book_form_validation_for_blank_items():
    form = AddPostForm(data={
        'title': '',
        'content': '',
    })
    assert not form.is_valid()
