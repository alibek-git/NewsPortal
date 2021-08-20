from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'dateCreated': ['day__gte', 'month__gte'],
            'categoryType': ['exact'],
            'author': ['exact'],
        }
