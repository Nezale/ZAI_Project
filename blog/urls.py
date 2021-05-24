from django.urls import include, path
from .views import PostCategoryList, PostCategoryDetail, PostDetail, PostList

urlpatterns = [
    path('post-categories', PostCategoryList.as_view(), name=PostCategoryList.name),
    path('post-categories/<int:pk>', PostCategoryDetail.as_view(), name=PostCategoryDetail.name),
    path('post/<int:pk>', PostDetail.as_view(), name=PostDetail.name),
    path('posts', PostList.as_view(), name=PostList.name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

