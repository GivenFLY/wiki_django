from rest_framework import serializers

from .models import *

class ArticleVersionSerializer(serializers.Serializer):
    class Meta:
        model = ArticleVersion

    title = serializers.CharField()
    text = serializers.CharField()
    number = serializers.CharField()


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        depth = 1

    id = serializers.IntegerField()
    current_version = ArticleVersionSerializer()
