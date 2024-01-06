from rest_framework import generics, permissions
from upvotes.models import Upvote
from upvotes.serializers import UpvoteSerializer


class UpvoteListView(generics.ListCreateAPIView):
    """
    Lists or create Upvotes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UpvoteSerializer  
    queryset = Upvote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)