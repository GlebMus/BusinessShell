from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, CommentCreateView

app_name = 'post'

urlpatterns = [
    path('api/create', PostCreateView.as_view(), name='create-post'),
    path('api/list/', PostListView.as_view(), name='all-posts'),
    path('api/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/comment/<int:pk>/', CommentCreateView.as_view(), name='post-detail'),
]