from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    # 데이터베이스로부터 모든 post를 다 받아올 예정
    qs = Post.objects.all()
    return render(request, 'blog1/post_list.html', {
        'post_list':qs,
        })