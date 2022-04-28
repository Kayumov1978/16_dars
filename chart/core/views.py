from multiprocessing import context
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp_s.html', context)

def slice(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'line.html', context)

def bars(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bar.html', context)

def radar(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'radar.html', context)

def pie(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pie.html', context)

def polar(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'polar.html', context)

def bublle(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bublle.html', context)

def area(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'area.html', context)