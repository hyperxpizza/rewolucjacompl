from django.db import models
from django.utils import timezone
from django.urls import reverse 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

#tags
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICE = (
        ('draft','Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=150, blank=True, null=True)
    #text = RichTextField(blank=True, null=True)
    text = RichTextUploadingField(blank=True, null=True)
    #text = models.TextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='published')

    objects = models.Manager()
    published = PublishedManager()

    #tags 
    tags = TaggableManager()

    class Meta:
        ordering=('created_at',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
   
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
