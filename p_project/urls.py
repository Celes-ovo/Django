# 이거 좀 고쳐야 함....급조한 거임...
# https://life-with-coding.tistory.com/464

from django.urls import path, include
from . import views
app_name = 'posts'
urlpatterns = [ path('index',views.index), ]