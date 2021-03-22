from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.request import Request

from .models import *
from .serializers import *

class ArticleListCreateAPIView(ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    def create(self, request, *args, **kwargs):
        title = request.query_params.get("title")
        text = request.query_params.get("text")
        if not title or not text:
            return Response({"error": "Fields title and text should be filled"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            v = ArticleVersion(title=title, text=text)
            a = Article()
            a.add_version(v)
            serializer = ArticleSerializer(a)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailUpdateAPIView(RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def put(self, request, *args, **kwargs):
        title = request.query_params.get("title")
        text = request.query_params.get("text")
        if not title or not text:
            return Response({"error": "Fields title and text should be filled"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            a = Article.objects.filter(id=kwargs.pop("pk"))
            if a:
                if a.current_version.title == title and a.current_version.text == text:
                    return Response(None, status=status.HTTP_204_NO_CONTENT)

                v = ArticleVersion(title=title, text=text)
                a[0].add_version(v)
                return Response(None, status=status.HTTP_204_NO_CONTENT)

            else:
                return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)


class ArticleVersionListAPIView(ListCreateAPIView):
    serializer_class = ArticleVersionSerializer

    queryset = ArticleVersion.objects.all()
    
    def list(self, request, *args, **kwargs):
        a = Article.objects.filter(id=kwargs.pop("pk"))
        if a:
            queryset = ArticleVersion.objects.filter(article_obj=a[0])
            serializer = ArticleVersionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        

class ArticleVersionDetailAPIView(RetrieveUpdateAPIView):
    def retrieve(self, request, *args, **kwargs):
        a = Article.objects.filter(id=kwargs.pop("pk"))
        if a:
            v = ArticleVersion.objects.filter(article_obj=a[0], number=kwargs.pop("number"))
            if v:
                serializer = ArticleVersionSerializer(v[0])
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({"error": "Version not found"}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, *args, **kwargs):
        a = Article.objects.filter(id=kwargs.pop("pk"))
        if a:
            v = ArticleVersion.objects.filter(article_obj=a[0], number=kwargs.pop("number"))
            if v:
                if a[0].current_version.number == v[0].number:
                    return Response("", status=status.HTTP_204_NO_CONTENT)
                a[0].current_version = v[0]
                a[0].save()
                return Response("", status=status.HTTP_204_NO_CONTENT)

            else:
                return Response({"error": "Version not found"}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)