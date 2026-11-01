from django.shortcuts import render
from .models import *
from .posts import *

def index(request):
    index = Post.objects.all()
    return render(request, 'allahHodbarh/index.html', {'index': index})