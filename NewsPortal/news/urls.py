from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>', PostDetailedView.as_view(), name='post'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/create/', PostUpdateView.as_view(), name='post_create'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', become_an_author, name='upgrade'),
    path('<int:pk>/', cache_page(60*10)(PostDetailedView.as_view()), name='product_detail'),
    # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.


]
