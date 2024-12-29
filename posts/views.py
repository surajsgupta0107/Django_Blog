from django.shortcuts import render

from posts.models import Post


def posts(request):
    context = {
        "title": "Posts",
        "block_title": "Posts Page",
        "posts": Post.objects.all(),
    }
    return render(request, "main/home.html", context)
