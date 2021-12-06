from django.urls import path
from . import views
from .views import BookmarkListView

urlpatterns = [
    path('', BookmarkListView.as_view(), name = 'list'),
    path('', views.index, name='index'),
]