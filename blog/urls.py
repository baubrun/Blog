from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", login_required(views.CreateBlogView.as_view()), name="post_new"),
    path("post/<int:pk>/edit/", views.EditBlogView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.DeleteBlogView.as_view(), name="post_delete"),
]
