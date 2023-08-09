from django.shortcuts import render

from django.views import View
from django.http import JsonResponse

# Create your views here.
from .models import MainView

def post_list(request):
    return render(request, 'pnet_test/post_list.html', {})

def post_answer(request):
    return render(request, 'pnet_test/answer.html', {})