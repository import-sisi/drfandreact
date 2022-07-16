from django.urls import path
from .views import AdminPostDetail, CreatePost, DeletePost, EditPost, PostList, PostDetail, PostListDetailfilter

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLS
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
    
]





# from .views import PostList, PostListDetailfilter
# from rest_framework.routers import DefaultRouter

# app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls



