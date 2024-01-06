from rest_framework import generics
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from mycar_drfapi.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    
    """
    List all profiles
    No create view as profile creation is handled by signals
    Orders profile list by creation in descending order
    """
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile
    Allows update of the profile
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
