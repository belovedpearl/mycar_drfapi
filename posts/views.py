from rest_framework import generics, permissions, filters
from mycar_drfapi.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class PostsList(generics.ListCreateAPIView):
    """
    Checks for permission allowed on user
    Gets all Post objects in a list
    Associates owner with the post
    """
   
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        upvotes_count= Count('upvotes', distinct=True),
        downvotes_count= Count('downvotes', distinct=True),
        reviews_count= Count('review', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        '^make',
        '^model',
        'owner__username',
        '^body_types',
        '^year'
    ]
    filterset_fields = [
        #user's feed
        'owner__followed__owner__profile',
        #user's upvoted post
        'upvotes__owner__profile',
        #user's downvoted post
        'downvotes__owner__profile',
        #posts
        'owner__profile',
        'body_types'     
    ]
    ordering_fields = [
        'upvotes_count',
        'downvotes_count',
        'upvotes__created_at',
        'downvotes__created_at',
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        upvotes_count= Count('upvotes', distinct=True),
        downvotes_count= Count('downvotes', distinct=True),
        reviews_count= Count('review', distinct=True)
    ).order_by('-created_at')