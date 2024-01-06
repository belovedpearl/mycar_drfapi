from rest_framework import generics
from upvotes.models import Upvote
from upvotes.serializers import UpvoteSerializer


class UpvoteListView(generics.ListCreateAPIView):
    """
    Lists or create Upvotes
    """
    serializer_class = UpvoteSerializer  
    queryset = Upvote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)