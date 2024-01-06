from rest_framework import generics, permissions
from downvotes.models import Downvote
from downvotes.serializers import DownvoteSerializer
from mycar_drfapi.permissions import IsOwnerOrReadOnly
from upvotes.models import Upvote
from rest_framework import serializers


class DownvoteListView(generics.ListCreateAPIView):
    """
    Lists or create Downvotes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DownvoteSerializer  
    queryset = Downvote.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data['post']
        # Check if the user has already upvoted
        if Upvote.objects.filter(owner=user, post=post).exists():
            raise serializers.ValidationError(
                {'details': 'Cannot downvote because you already upvoted this post'}
            )
        serializer.save(owner=self.request.user)
        

class DownvoteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a downvote or delete if user is the owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DownvoteSerializer
    queryset = Downvote.objects.all()
