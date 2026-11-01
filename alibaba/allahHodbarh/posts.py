from django import posts
from .models import Post

class PostsPost(posts.ModelPost):
    class Meta:
        model = Post
        field = ['title', 'content', 'genre']
        widgets = {
            'title': posts.TextInput(attrs={'class':'posts-control'}),
            'content': posts.TextInput(attrs={'class':'posts-control'}),
            'genre': posts.TextInput(attrs={'class':'posts-control'}),
        }