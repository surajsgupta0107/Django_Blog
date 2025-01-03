from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from posts.models import Post


def home(request):
    context = {
        "title": "Home",
        "block_title": "Home Page",
        "posts": Post.objects.all().order_by("-date_posted"),
    }
    return render(request, "main/home.html", context)


class PostListView(ListView):
    model = Post
    # defaults can be customized
    template_name = "main/home.html"  # <app>/<model>_<viewtype>.html  # posts/post_list.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # defaults can be customized
    template_name = "posts/user_posts.html"  # <app>/<model>_<viewtype>.html  # posts/post_list.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post
    # defaults can be customized
    # template_name = "main/post_detail.html"  # <app>/<model>_<viewtype>.html  # posts/post_detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # defaults can be customized
    # template_name = "main/post_form.html"  # <app>/<model>_<viewtype>.html  # posts/post_form.html
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # defaults can be customized
    # template_name = "main/post_form.html"  # <app>/<model>_<viewtype>.html  # posts/post_form.html
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # defaults can be customized
    # template_name = "main/post_confirm_delete.html"  # <app>/<model>_<viewtype>.html  # posts/post_confirm_delete.html
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        "title": "About",
        "block_title": "About Page",
    }
    return render(request, "main/about.html", context)
