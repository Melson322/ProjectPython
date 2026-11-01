from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'allahHodbarh/index.html', {'posts': posts})