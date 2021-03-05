from django.contrib import admin
from .models import Movie, DoubanComment


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movieId', 'title', 'directors',
                    'year', 'casts', 'region', 'types', 'rate']


class DoubanCommentAdmin(admin.ModelAdmin):
    list_display = ['movie', 'username', 'avatar', 'rate', 'time', 'content']


admin.site.register(Movie, MovieAdmin)
admin.site.register(DoubanComment, DoubanCommentAdmin)
