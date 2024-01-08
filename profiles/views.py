from rest_framework import generics, filters
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from mycar_drfapi.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    
    """
    List all profiles
    No create view as profile creation is handled by signals
    Orders profile list by creation in descending order
    """
    # queryset = Profile.objects.all().order_by('-created_at')
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),
        upvotes_count = Count('owner__upvote', distinct=True),
        downvotes_count = Count('owner__downvote', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile
    Allows update of the profile
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
