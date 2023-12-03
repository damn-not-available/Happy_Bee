from rest_framework import serializers
from .models import *

# 전체 조회
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')
        read_only_fields = ('user', 'like_users')


class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title',)

    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'like_users')
        


# 특정 게시물 조회
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users')



 
 