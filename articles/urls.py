from django.urls import path

from .views import *

app_name = "articles"

urlpatterns = [
    path('articles', ArticleListCreateAPIView.as_view(), name="list"),
    path('articles/<int:pk>', ArticleDetailUpdateAPIView.as_view(), name="detail"),
    path('articles/<int:pk>/<int:number>', ArticleVersionDetailAPIView.as_view(), name="version-detail"),
    path('articles/<int:pk>/versions', ArticleVersionListAPIView.as_view(), name="version-list"),
]
