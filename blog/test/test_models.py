import pytest

from blog.models import Post


@pytest.mark.django_db
class TestCatalogModel:
    """Тесты модели Catalog"""

    @pytest.fixture
    def post(self):
        """Создание тестовой книги без сохранения в БД"""
        return Post(
            title='First Django Book',
            content='978-1-60309-3',
        )

    def test_create_book_instance(self, post):
        """Экземпляр должен быть объектом Catalog"""
        assert isinstance(post, Post)

    def test_str_representation(self, post):
        """Проверка строкового представления"""
        assert str(post) == 'First Django Book'

    def test_saving_and_retrieving_book(self, django_db_setup, django_db_blocker):
        """Сохранение и получение книг из базы данных"""
        with django_db_blocker.unblock():
            # Создаем и сохраняем первую книгу
            first_book = Post.objects.create(
                title='First Django Book',
                content='978-1-60309-3',
            )

            # Создаем и сохраняем вторую книгу
            second_book = Post.objects.create(
                title='Second Django Book',
                content='978-3-60124-12',
            )

        # Получаем все книги из БД
        saved_books = Post.objects.all()
        assert saved_books.count() == 2

        # Проверяем сохраненные данные
        assert saved_books[0].title == 'First Django Book'
        assert saved_books[1].content == '978-3-60124-12'
