from django.shortcuts import render

from blog.forms import AddPostForm
from blog.models import Post


def blog(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'blog/post_list.html', {'posts': posts})


def post(request, id):
    post = Post.objects.get(id=id)  # Получаем все посты
    form = AddPostForm()
    return render(request, 'blog/post.html', {'post': post, 'form': form})
