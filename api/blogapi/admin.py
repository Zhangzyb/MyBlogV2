from django.contrib import admin
from .models import Article, ArticleDetail, Tag, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'abstract',
                    'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'image', 'category', 'tag']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class DetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'text']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'text', 'id', 'email', 'article',
                    'created_time', 'parent_comment']
    fields = ['username', 'email', 'text', 'article', 'status','parent_comment','images']


admin.site.register(Article, PostAdmin)
admin.site.register(ArticleDetail, DetailAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
