from django.db import models

from django.conf import settings
from django.utils import timezone

# Create your models here.
# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

# class Post(models.Model):
#     # 다른 모델에 대한 링크를 의미함.
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
#     # 글자 수가 제한된 텍스트를 정의할 때 사용
#     title = models.CharField(max_length=200)
#     # 글자 수에 제한이 없는 긴 텍스트를 정의할 때 사용
#     text = models.TextField()

#     # 날짜와 시간
#     created_date = models.DateTimeField(
#         default=timezone.now)
#     published_date = models.DateTimeField(
#         blank=True, null=True)

#     ## for test
#     class Users(models.Model):
#         value_1 = models.IntegerField()
#         value_2 = models.IntegerField()
#         value_out = models.IntegerField()

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

import threading
from time import sleep

ds_lock = threading.Lock()

class MainView(models.Model):
    value_1 = models.CharField(max_length=200, default='')
    value_2 = models.CharField(max_length=200, default='')
    output = models.CharField(max_length=200, default='')

    def add(self, *args):
        input_1 = self.value_1
        input_2 = self.value_2

        output = input_1 + input_2

        print('========')
        print(output)

        self.output = output
        super().save(force_update=True)

        ds_lock.release()