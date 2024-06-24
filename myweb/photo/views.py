from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    # get_object_or_404 = Model로부터 데이터를 찾아보고, 만약 찾는 데이터가 없다면 404 error를 반환
    # pk = Model의 데이터들을 구분하는 Django의 기본 ID 값
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})