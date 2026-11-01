from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4500)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=5)

    def __srt__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField(max_length=3500)
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.content