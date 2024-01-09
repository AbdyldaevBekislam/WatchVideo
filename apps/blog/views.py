from django.shortcuts import render

from apps.blog.models import Blog

def index(request):
    return render(request, "index.html")

