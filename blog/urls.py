from django.urls import path

from blog.views import blog, post
app_name = 'blog'  # Здесь мы устанавливаем пространство имен для приложения
urlpatterns = [
    path('', blog, name='post_list'),
    path('post/<slug:slug>', post, name='post'),
]
