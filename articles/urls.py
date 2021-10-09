from django.urls import path

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    #path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'), # without slug
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail'), # using slug
    path('', ArticleListView.as_view(), name='article_list'),
]