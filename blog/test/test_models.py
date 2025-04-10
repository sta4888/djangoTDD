import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from blog.models import Post


# проверка модели БД
@pytest.mark.django_db
def test_can_create_post():
    post = Post.objects.create(
        title="Заголовок поста",
        slug="zagolovok-posta",
        content="Тело поста"
    )
    assert Post.objects.count() == 1
    assert post.title == "Заголовок поста"

@pytest.mark.django_db
def test_post_requires_title_and_slug():
    with pytest.raises(IntegrityError):
        Post.objects.create(content="Тело без заголовка и слага")


def test_post_str_returns_title():
    post = Post(title="Привет", slug="privet", content="...")
    assert str(post) == "Привет"


def test_post_slug_is_unique(db):
    Post.objects.create(title="1", slug="same", content="...")
    with pytest.raises(IntegrityError):
        Post.objects.create(title="2", slug="same", content="...")

@pytest.mark.skip
def test_post_ordering(db):
    p1 = Post.objects.create(title="A", slug="a", content="...")
    p2 = Post.objects.create(title="B", slug="b", content="...")
    posts = list(Post.objects.all())
    assert posts == [p2, p1]  # если ordering = ['-id'] например

@pytest.mark.skip
def test_post_created_and_updated_set_automatically(db):
    post = Post.objects.create(title="...", slug="...", content="...")
    assert post.created is not None
    assert post.updated is not None


@pytest.mark.django_db
def test_post_requires_title_and_slug():
    post = Post(content="...")
    with pytest.raises(ValidationError):
        post.full_clean()  # вызывает валидацию модели


@pytest.mark.skip
def test_post_slug_required_in_db():
    with pytest.raises(IntegrityError):
        Post.objects.create(title="", content="...")  # нет slug