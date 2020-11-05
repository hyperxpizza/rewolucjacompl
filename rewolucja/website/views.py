from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from taggit.models import Tag
import random

from .models import Post, Subscriber

#helpers
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

def index(request):
    context = {}
    return render(request, 'website/index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug)

    #increment hits counter
    post.hits += 1

    context = {
        'post': post
    }

    return render(request, 'website/post_detail.html', context)

def view_by_tag(request, slug):
    tag = Tag.objects.filter(slug=slug).values_list('name', flat=True)
    name = slug
    post_list = Post.objects.filter(tags__name__in=tag, status="published")

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'name': name,
        'tag': tag,
        'posts': posts
    }

    return render(request, 'publishing/view_by_tag.html', context)

def art(request):
    context = {}
    return render(request, 'website/art.html', context)

def store(request):
    context = {}
    return render(request, 'website/store.html', context)

def product_detail(request, slug):
    context = {}
    return render(request, 'website/product_detail', context)

def about(request):
    context = {}
    return render(request, 'website/about.html', context)

@csrf_exempt
def newsletter_signup(request):
    if request.method == "POST":
        new_subscriber = Subscriber(email=request.POST["email"], conf_num=random_digits())
        new_subscriber.save()
        new_subscriber.send_welcome_email()

@csrf_exempt
def unsubscribe_newsletter(request, conf_num):
    pass