from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, AutorForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'myapp/post_edit.html', {'form': form})

def autores_new(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = AutorForm()
    return render(request, 'myapp/autores_edit.html', {'form': form})