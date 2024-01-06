from rest_framework import generics, permissions
from mycar_drfapi.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostsList(generics.ListCreateAPIView):
    """
    Checks for permission allowed on user
    Gets all Post objects in a list
    Associates owner with the post
    """
   
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all().order_by('-created_at')