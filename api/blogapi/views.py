from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.filters import BaseFilterBackend
from rest_framework import status

from drf_haystack.viewsets import HaystackViewSet
from .serializer import ArticleSerializer, ArticleDetailSerializer, CommentSerializer, PostCommentSerializer, TimeSerializer, DynamicSerializer, CategorySerializer, SearchSerializer
from .models import Article, Comment, Category


class CommentFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        article = request.query_params.get('article')
        comment_id = request.query_params.get('comment_id')
        if article:
            return queryset.filter(article=article).filter(parent_comment=None)
        elif comment_id:
            return queryset.filter(parent_comment=comment_id)
        return queryset


class ArticleView(ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('-created_time')
    serializer_class = ArticleSerializer

    def get_serializer_class(self):
        pk = self.kwargs.get('pk')
        if pk:
            return ArticleDetailSerializer
        return ArticleSerializer


class CommentView(ListCreateAPIView, UpdateAPIView):
    queryset = Comment.objects.filter(status=0).order_by('-created_time')
    serializer_class = None
    pagination_class = None
    filter_backends = [CommentFilterBackend, ]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCommentSerializer
        return CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        new_ins = serializer.save()
        obj = CommentSerializer(instance=new_ins)
        return obj


class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        data_list = []
        data_dict = {}
        for query in queryset:
            data = Article.objects.filter(
                category=query).order_by('-created_time')
            ser = CategorySerializer(instance=data, many=True)
            if ser.data:
                data_dict['category'] = query.name
                data_dict['data'] = ser.data
                data_list.append(data_dict)
                data_dict = {}
        return Response(data_list)


class TimeView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Comment.objects.dates('created_time', 'year').reverse()
        data_list = []
        data_dict = {}
        for query in queryset:
            data = Comment.objects.filter(
                created_time__year=query.year, status=1).order_by('-created_time')
            ser = TimeSerializer(instance=data, many=True)
            if ser.data:
                data_dict['time'] = query.year
                data_dict['data'] = ser.data
                data_list.append(data_dict)
                data_dict = {}
        return Response(data_list)


class DynamicView(ListAPIView):
    queryset = Comment.objects.filter(status=2).order_by('-created_time')
    serializer_class = DynamicSerializer


class SearchView(HaystackViewSet):
    index_models = [Article]
    serializer_class = SearchSerializer
    pagination_class = None
