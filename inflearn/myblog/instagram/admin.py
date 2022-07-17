from django.contrib import admin
from .models import Post

# Register your models here.

# 방법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 필드가 나오게 됨.
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']

    # 메세지에 링크를 만들어주는 역할
    list_display_links = ['message']

    # search_fields 속성
	search_fields = ['message']

    # list_filter 속성
    list_filter = ['created_at']

# 방법 1
# admin.site.register(Post)

# 방법 2
# admin.site.register(Post, PostAdmin)