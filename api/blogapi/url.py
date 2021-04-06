from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"search", views.SearchView, basename="search")

app_name = 'blogapi'
urlpatterns = [
    path('home/posts/', views.ArticleView.as_view({'get': 'list'})),
    path('home/posts/<int:pk>/',
         views.ArticleView.as_view({'get': 'retrieve'})),
    path('comments/', views.CommentView.as_view()),
    path('comments/<int:pk>/', views.CommentView.as_view()),
    path('time/', views.TimeView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('dynamic/', views.DynamicView.as_view()),
    path('',include(router.urls))
    # path('search/', include('haystack.urls')),
    # path('', views.index, name='index'),
    # path('articles/<slug:english_name>/', views.detail, name='detail'),
    # path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    # path('tags/<slug:name>/', views.tag, name='tag'),
    # path('category/<slug:cate_name>/', views.category, name='category'),
    # path('article/inc_like/<slug:english_name>/', views.add_likes, name='likes'),
]
