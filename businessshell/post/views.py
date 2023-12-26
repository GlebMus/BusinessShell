from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Post, Comment
from .serializers import PostSerializers, PostsSerializers, CommentSerializer


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAdminUser]


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializers


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all().prefetch_related('comment')
    serializer_class = PostSerializers


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        serializer.save(post_id=post_id)