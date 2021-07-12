from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def bloghome(request):
    posts=Post.objects.all()
    # print(posts)
    context={'posts': posts}
    return render(request,'blog/blog.html', context)
     

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={'post':post}
    # print(post)
    return render(request,'blog/blogpost.html',context)
