# from django.urls import path

# from mysite import views


# app_name = 'mysite'
# urlpatterns = [
#     path('post/<int:pk>/', views.PostDetailTV.as_view(), name='post_detail'),
# ]

from rest_framework import routers
from django.urls import path, include

from mysite.views import UserViewSet

# Routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]