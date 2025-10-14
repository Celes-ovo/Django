# views.py 파일 내에 정의한 특정 함수를 실행하기 위해 해당되는 정규 표현식을 요청에 지정하는 URL 패턴을 정의

# from django.conf.urls import url
from django.urls import re_path
from games import views

# urlpatterns 리스트를 사용하면 URL을 view로 보낼 수 있음
# 해당 정규 
urlpatterns = [
    re_path(r'^games/$', views.game_list),
    re_path(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
]