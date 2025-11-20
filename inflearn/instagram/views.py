# render : 템플릿 렌더링 (html)
# 특정 HTML 템플릿에 데이터를 채워넣고, 그 결과를 HttpResponse 객체로 반환하는 단축 기능
# get_object_or_404 : 특정 객체 가져오기, 없으면 404 에러 발생
from django.shortcuts import render, get_object_or_404
from .models import Post

from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import DetailView

# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    # query
    q = request.GET.get('q', '')

    if q:
        qs = qs.filter(message__icontains = q)
    
    return render(request, 'instagram/post_list.html', {
        'post_list':qs,
        'q':q,
    })

# def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except:
#     #     raise Http404("포스트를 찾을 수 없습니다.")
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post':post,
#     })


post_detail = DetailView.as_view(model=Post)


#
def archives_year(request, year):
    return HttpResponse(f'{year}년의 아카이브입니다.')