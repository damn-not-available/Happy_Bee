from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ArticleList.as_view(actions={
    #     'get': 'retrieve',
    #     'post': 'create',
    #     })),
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('category/<int:category_pk>/', views.category_list),
    path('<int:article_pk>/comments/', views.comment_list),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
]
