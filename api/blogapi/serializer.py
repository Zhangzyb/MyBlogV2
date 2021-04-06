from rest_framework import serializers
from rest_framework.serializers import CharField
from drf_haystack.serializers import HaystackSerializerMixin
from django.utils import timezone
from blogapi import models
from .utils import Highlighter


class HighlightedCharField(CharField):
    def to_representation(self, value):
        value = super().to_representation(value)
        request = self.context["request"]
        query = request.query_params["text"]
        highlighter = Highlighter(query)
        return highlighter.highlight(value)


class ArticleSerializer(serializers.ModelSerializer):
    time_format = serializers.SerializerMethodField()
    comment_num = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'image', 'time_format',
                  'abstract', 'views', 'likes', 'comment_num']

    def get_time_format(self, obj):
        now = timezone.now()
        diff = now - obj.created_time
        if diff.days == 0:
            if diff.seconds < 60:
                return '刚刚'
            elif diff.seconds < 3600:
                return str(diff.seconds // 60) + '分钟前'
            else:
                return str(diff.seconds // 3600) + '个小时前'
        elif 1 <= diff.days <= 31:
            return str(diff.days) + '天前'
        elif diff.days < 186:
            return str(diff.days // 30) + '个月前'
        else:
            return obj.created_time

    def get_comment_num(self, obj):
        comment_num = obj.comment_set.all().count()
        return comment_num


class ArticleDetailSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='articledetail.text')
    category = serializers.CharField(source='category.name')
    tag_info = serializers.SerializerMethodField()
    comment_num = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'created_time', 'category',
                  'content', 'tag_info', 'views', 'likes', 'comment_num']

    def get_tag_info(self, obj):
        return [item for item in obj.tag.all().values('id', 'name')]

    def get_comment_num(self, obj):
        comment_num = obj.comment_set.filter(status=0).count()
        return comment_num


class CommentSerializer(serializers.ModelSerializer):
    sub_comment_num = serializers.SerializerMethodField()
    created_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Comment
        exclude = ['images']

    def get_sub_comment_num(self, obj):
        sub_comment_num = models.Comment.objects.filter(
            parent_comment=obj.id).count()
        return sub_comment_num

    def get_created_time(self, obj):
        now = timezone.now()
        diff = now - obj.created_time
        if diff.days == 0:
            if diff.seconds < 60:
                return '刚刚'
            elif diff.seconds < 3600:
                return str(diff.seconds // 60) + '分钟前'
            else:
                return str(diff.seconds // 3600) + '个小时前'
        elif 1 <= diff.days <= 31:
            return str(diff.days) + '天前'
        elif diff.days < 186:
            return str(diff.days // 30) + '个月前'
        else:
            return obj.created_time


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['username', 'email', 'text',
                  'article', 'parent_comment', 'reply_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'created_time', 'image', 'abstract']


class TimeSerializer(serializers.ModelSerializer):
    created_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Comment
        exclude = ['images']

    def get_created_time(self, obj):
        month = obj.created_time.month
        day = obj.created_time.day
        time = obj.created_time.strftime('%H:%M')
        return f'{month}月{day}日 {time}'


class DynamicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class SearchSerializer(HaystackSerializerMixin, CategorySerializer):
    title = HighlightedCharField()
    abstract = HighlightedCharField(source='articledetail.text')

    class Meta(CategorySerializer.Meta):
        search_fields = ["text"]
        fields = ["id","title","abstract","image","created_time"]
