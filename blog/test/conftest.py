
import pytest
from blog.models import Post

@pytest.fixture
@pytest.mark.django_db
def catalog_instance():
    """Создание экземпляра поста для использования в тестах"""
    return Post.objects.create(
        title='Test Post',
        content='This is a test post.',
    )
