from django.db import IntegrityError
from rest_framework import serializers
from downvotes.models import Downvote


class DownvoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Downvote model
    Owner field is ReadOnly to prevent change
    Allows one vote on a post via the integrity constraint
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Downvote
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'details': 'Your vote is already registered'}
            )
