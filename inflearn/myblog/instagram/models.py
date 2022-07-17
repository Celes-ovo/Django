from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField() # default : blank=False
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Java의 toString
    def __str__(self):
        #return f"Custom post object ({self.id})"
        return self.message

    # admin.py에 구현할 수도 있지만, 이번에는 model.py에 구현하기로 함.
    def message_length(self):
        #return len(self.message)
        return f'{len(self.message)}글자'

    # short_description
    message_length.short_description = '메세지 글자 수'