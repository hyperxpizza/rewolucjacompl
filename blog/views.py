from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm

from taggit.models import Tag

def all_posts(request, tag_slug=None):
    posts = Post.objects.all().order_by("-created_at")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = object_list.filter(tags__in=[tag])

    context = {
        'posts': posts,
        'tag': tag,
    }

    return render(request, 'blog/all_posts.html', context)

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)

    new_comment = None
    comments = post.comments.filter(active=True)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm() 
    
    context={
        'post':post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    
    return render(request, 'blog/post_detail.html', context)