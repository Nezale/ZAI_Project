from django.urls import include, path
from .views import PostCategoryList, PostCategoryDetail, PostDetail, PostList, AuthorList, UserList, UserDetail, ApiRoot, AuthorDetail

urlpatterns = [
    path('authors', AuthorList.as_view(), name=AuthorList.name),
    path('author/<int:pk>', AuthorDetail.as_view(), name=AuthorDetail.name),
    path('user/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('users', UserList.as_view(), name=UserList.name),
    path('post-categories', PostCategoryList.as_view(), name=PostCategoryList.name),
    path('post-categories/<int:pk>', PostCategoryDetail.as_view(), name=PostCategoryDetail.name),
    path('post/<int:pk>', PostDetail.as_view(), name=PostDetail.name),
    path('posts', PostList.as_view(), name=PostList.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

