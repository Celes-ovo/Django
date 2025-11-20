from . import views
from django.urls import include, path, register_converter

# from debug_toolbar.toolbar import debug_toolbar_urls

# urlpatterns = [
#     path('', views.post_list)    
# ] + debug_toolbar_urls()


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        # 4자리 맞춤
        # return "%04d" % value
        return str(value)
    
register_converter(YearConverter, 'year')



urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),

    #
    # path('archives/<int:year>/', views.archives_year),
    path('archives/<year:year>/', views.archives_year)
]