from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='한 문장으로 표현해보세요')

    def __str__(self):
        return self.name
    

class Article(models.Model):
    # 작성자를 외래키로 설정
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    # N:M
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles'
    )

    # fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # 어떤 글에 댓글을 작성할지? -> 글을 외래키로 설정
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    # 작성자를 외래키로 설정
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # N:M
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_comments'
    )
    # fields
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

