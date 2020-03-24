from django.shortcuts import render
from .models import Post

# Create your views here.

def post(request):
    posts = Post.objects.order_by('created')
    return render(request,'first/post.html', {'posts':posts})