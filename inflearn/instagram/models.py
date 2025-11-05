from django.db import models

# Create your models here.
class Post(models.Model):
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