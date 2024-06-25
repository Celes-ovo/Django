from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    # get_object_or_404 = Model로부터 데이터를 찾아보고, 만약 찾는 데이터가 없다면 404 error를 반환
    # pk = Model의 데이터들을 구분하는 Django의 기본 ID 값
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})

def photo_post(request, pk):
    # 수정할 대상을 pk를 이용하여 찾아 옴.
    photo = get_object_or_404(Photo, pk=pk)

    # 들어온 요청이 POST일 경우
    if request.method == "POST":
        form = PhotoForm(request.POST)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            return redirect('photo_detail', pk = photo.pk)
    
    # 들어온 요청이 GET일 경우    
    else:
        # photo data를 PhotoForm에 담아서 넘겨 줌.
        form = PhotoForm(instance=photo)
    
    return render(request, 'photo/photo_post.html', {'form':form})


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            return redirect('photo_detail', pk=photo.pk)
        
    else:
        form = PhotoForm(instance=photo)
    
    return render(request, 'photo/photo_post.html', {'form':form})