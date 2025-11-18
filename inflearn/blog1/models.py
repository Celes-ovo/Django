from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='+')
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add : 모델 객체가 최초 생성될 때의 현재 시각을 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 모델 객체가 저장될 때마다 현재 시각을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True)