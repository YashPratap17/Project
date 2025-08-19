from django.shortcuts import render
from django.http import HttpResponse

def blog_index(request):
    return render(request=request, template_name='blog_index.html')
def list_posts(request):
    return render(request=request, template_name='posts.html')    