from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path
# from .views import (
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
# )
# from . import views

urlpatterns = [
    # path("", views.posts, name="posts-posts"),
    # path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("post/create/", PostCreateView.as_view(), name="post-create"),
    # path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    # path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
