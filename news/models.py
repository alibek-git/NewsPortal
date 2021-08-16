from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)


class Category(models.Model):
    general = 'GEN'
    science = 'SCI'
    culture = 'CUL'
    sports = 'SPO'
    politics = 'POL'
    CATEGORIES = [(general, 'General'), (science, 'Science'), (culture, 'Culture'),
                  (sports, 'Sports'), (politics, 'Politics')]
    name = models.CharField(max_length=3, choices=CATEGORIES, default=general, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NEW'
    ARTICLE = 'ART'
    CATEGORY_CHOICES = [(NEWS, 'NEWS'), (ARTICLE, 'ARTICLE'), ]
    category_type = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=NEWS)
    dateCreated = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)