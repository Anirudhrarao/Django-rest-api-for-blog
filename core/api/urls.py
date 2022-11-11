from django.urls import path
from core.api.views import (UserAPIList, 
                            UserAPIDetail,
                            PostAPIList, 
                            PostAPIDetail, 
                            CommentAPIList, 
                            CommentAPIDetail,
                            CategoryAPIList,
                            CategoryAPIDetail)

urlpatterns = [
    path('user/',UserAPIList.as_view(),name='user-list'),
    path('user/<int:pk>/',UserAPIDetail.as_view(),name='user-detail'),
    path('post/',PostAPIList.as_view(),name='post-list'),
    path('post/<int:pk>/',PostAPIDetail.as_view(),name='post-detail'),
    path('comment/',CommentAPIList.as_view(),name='comment-list'),
    path('comment/<int:pk>/',CommentAPIDetail.as_view(),name='comment-detail'),
    path('category/',CategoryAPIList.as_view(),name='category-list'),
    path('category/<int:pk>/',CategoryAPIDetail.as_view(),name='category-detail')
]
