from rest_framework import generics, permissions
from reviews.models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from mycar_drfapi.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



class ReviewList(generics.ListCreateAPIView):
    """
    List reviews or create a review if logged in.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post',  
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves a review, allows update or delete if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()