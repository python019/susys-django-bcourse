from django.shortcuts import render

from .models import Post

def home(request):
    data = Post.objects.all()
    return render(request, "home.html", {'posts': data})

def single(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, "single.html", {'post': data})


