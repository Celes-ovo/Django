# Register your models here.
from django.contrib import admin
from .models import Post, Comment, Tag

#
from django.utils.safestring import mark_safe

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'image', 'image_tag', 'is_public', 'created_at', 'updated_at']
    # 
    list_diaplay_links = ['message']
    list_filter = ['is_public']

    def image_tag(self, post):
        if post.image:
            return mark_safe(f'<img src="{post.photo.url}" style="width=75px" />')

    def message_length(self, post):
        return f'{len(post.message)}'
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass