from django.shortcuts import render
from django.http import HttpResponse
from curiosity.models import Post, Category

# Create your views here.
def home(request):
    # load all the posts from db(10)
    posts = Post.objects.all()
    # print(posts)

    # load all categories
    cats = Category.objects.all()

    data = {
        'posts':posts,
        'cats': cats
    }
    return render(request, 'home.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    # print(post)
    return render(request,'posts.html',{'post':post, 'cats':cats})


def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat, 'posts':posts})

# This was written by Sushant Abrin

def index(request):
    return render(request,'index.html')
