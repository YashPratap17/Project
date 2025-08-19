from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Posts

def blog_index(request):
    return render(request=request, template_name='blog_index.html')
def list_posts(request):
    return render(request=request, template_name='blog/posts.html')