from . import views
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', views.post_list)    
] + debug_toolbar_urls()

# urlpatterns = [
#     path('', views.post_list)    
# ]