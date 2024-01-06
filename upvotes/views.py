from rest_framework import generics
from upvotes.model import Upvote
from upvote.serializers import UpvoteSerializer


class UpvoteListView(generics.ListCreateAPIView):
    """
    Lists or create Upvotes
    """
    serializer_class = UpvoteSerializer  
    queryset = Upvote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)