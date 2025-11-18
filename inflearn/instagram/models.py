from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(blank=True)
    image_tag = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # JAVA의 toString과 유사
    def __str__(self):
        return f'Post object ({self.id})'
    
    # Test 용도
    def meassage_text(self):
        return self.message
    
    class Meta:
        ordering = ['-id']



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public':True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment object ({self.id})'
    
    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name