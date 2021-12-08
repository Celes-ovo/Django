from django.shortcuts import render
from django.http import HttpResponse

#from p_project.bookmark.models import Bookmark

# Create your views here.
def index(request):
    #return HttpResponse("Polls index")
    return render(request, 'bookmark/bookmark_list.html')

from django.views.generic.list import ListView
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark