from django.contrib import admin
from .models import Article, Tag, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    fields = ['title', 'image', 'text', 'category', 'tag']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','parent']
    fields = ['name','parent']

admin.site.register(Article, PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)