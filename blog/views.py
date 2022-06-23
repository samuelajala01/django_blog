from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from django.db import models

# Create your views here.
class PostListView(ListView):
  model=Post

class PostCreateView(CreateView):
  model = Post
  fields = __all__
  success_url  = reverse_lazy("blog:all")  

class PostDetailView(generic.edit.DeleteView):
  model = Post

class PostUpdateView(UpdateView):
  model = Post
  fields = "__all__"
  success_url  = reverse_lazy("blog:all") 

class PostDeleteView(UpdateView):
  model = Post
  fields = "__all__"
  success_url  = reverse_lazy("blog:all") 