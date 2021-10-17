from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView# new
from django.urls import reverse_lazy # new
from .models import Post
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name='posts'
    

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
    context_object_name='post'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url = reverse_lazy('home')