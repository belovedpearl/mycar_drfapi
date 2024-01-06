from rest_framework import generics, permissions
from reviews.models import Review
from .serializers import ReviewSerializer



class ReviewList(generics.ListCreateAPIView):
    """
    List reviews or create a review if logged in.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
