from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>', PostDetailedView.as_view()),
    path('search/', PostSearchView.as_view()),
]
