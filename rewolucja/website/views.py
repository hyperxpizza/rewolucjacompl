from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from .models import Post


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
