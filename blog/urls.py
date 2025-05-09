from django.urls import path

from .views import *

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
