from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>', PostDetailedView.as_view(), name='post'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/create/', PostUpdateView.as_view(), name='post_create'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
