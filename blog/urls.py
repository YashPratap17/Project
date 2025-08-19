from django.urls import path
from .views import blog_index, list_posts
urlpatterns = [
    path('', blog_index),
    path('posts/', list_posts),
]