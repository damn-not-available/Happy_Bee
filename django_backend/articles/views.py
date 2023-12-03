from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.authentication import TokenAuthentication

from .serializers import *
from .models import Article

# 인증된(로그인된) 사용자만 접근 가능
# @permission_classes([IsAuthenticated])
# class ArticleList(ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer()

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(instance=articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(instance=article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if article.user == request.user:
            article.delete()
            return Response( 
                {'delete': f'{article_pk}번 게시글이 삭제되었습니다'}, 
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {'message': '게시글 작성자가 아닙니다'},
            )

    elif request.method == 'PUT':
        # 원래 건 첫번째 인자로, 수정값은 data인자로
        if article.user == request.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(
                {'message': '게시글 작성자가 아닙니다'}
            )
        

@api_view(['GET'])        
def category_list(request, category_pk):
    article = Article.objects.filter(category=category_pk)
    serializer = ArticleListSerializer(article, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    # if request.method == 'GET':
    #     serializer = CommentSerializer(comments)
    #     return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['DELETE', 'POST'])
def comment_detail(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = get_object_or_404(article, pk=comment_pk)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
