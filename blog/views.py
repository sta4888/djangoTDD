from django.shortcuts import render

from blog.models import Post


def blog(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'blog/post_list.html', {'posts': posts})


def post(request, slug=None):
    post = Post.objects.get(slug=slug)  # Получаем все посты
    return render(request, 'blog/post.html', {'post': post})
