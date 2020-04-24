from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class CreateBlogView(CreateView):
     model = Post
     template_name = "post_new.html"
     fields = "__all__"

class EditBlogView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["body", "title"]   
    
    
class DeleteBlogView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")