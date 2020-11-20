from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from taggit.models import Tag
from .cart import Cart
import random

from .models import Post, Subscriber, ArtItem

#helpers
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

def index(request):
    all_posts = Post.objects.filter(status="published").order_by('-created_at')
    main_post = all_posts[0]
    featured_posts = all_posts [1:4]

    post_list = all_posts[4:0]

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'main_post': main_post,
        'featured_posts': featured_posts,
        'posts': posts
    }
    return render(request, 'website/index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

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
    art_items = ArtItem.objects.filter(visible=True).order_by('created_at')
    context = {
        'art_items': art_items
    }
    return render(request, 'website/art.html', context)

def store(request):
    context = {}
    return render(request, 'website/store.html', context)

def order_create(request):
    pass

def send_order_confirmation(order):
    pass

def send_order_notification(order):
    pass

def product_detail(request, slug):
    context = {}
    return render(request, 'website/product_detail', context)

def about(request):
    context = {}
    return render(request, 'website/about.html', context)

def search(request):
    pass

@csrf_exempt
def newsletter_signup(request):
    if request.method == "POST":
        new_subscriber = Subscriber(email=request.POST["email"], conf_num=random_digits())
        new_subscriber.save()
        new_subscriber.send_welcome_email()

@csrf_exempt
def unsubscribe_newsletter(request, conf_num):
    #find subscriber with given conf num
    subscriber = get_object_or_404(Subscriber, conf_num)
    subscriber.confirmed = False
    return render(request, 'website/unsubscribe.html')