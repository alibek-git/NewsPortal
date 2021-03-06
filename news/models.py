from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Sum
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import UserCreationForm
from django import forms
from allauth.account.forms import SignupForm


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)
    first_name = User.first_name
    last_name = User.last_name

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all().aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f'{self.authorUser.username}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True, blank=True)
    subscribers = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NEW'
    ARTICLE = 'ART'
    CATEGORY_CHOICES = [(NEWS, 'NEWS'), (ARTICLE, 'ARTICLE'), ]
    categoryType = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=NEWS)
    dateCreated = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title}'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.commentUser.username}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
