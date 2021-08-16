from django.db import models


class Author(models.Model):
    pass


class Category(models.Model):
    general = 'GEN'
    science = 'SCI'
    culture = 'CUL'
    sports = 'SPO'
    politics = 'POL'
    CATEGORIES = [(general, 'General'), (science, 'Science'), (culture, 'Culture'),
                  (sports, 'Sports'), (politics, 'Politics')]
    name = models.CharField(max_length=3, choices=CATEGORIES, default=general)


class Post(models.Model):
    pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    pass
