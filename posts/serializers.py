from rest_framework import serializers
from posts.models import Post
from upvotes.models import Upvote
from downvotes.models import Downvote
from reviews.models import Review

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer used for the model Post.
    Includes fields for the post information such as owner, owner's profile details,
    and a method field to check if the user is the post owner.
    Ensures image is included in the post and of the required dimension
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source = 'owner.profile.id')
    location = serializers.ReadOnlyField(source = 'owner.profile.location')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    image = serializers.ImageField(required=True)
    upvote_id = serializers.SerializerMethodField()
    downvote_id = serializers.SerializerMethodField()
    upvotes_count = serializers.ReadOnlyField()
    downvotes_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is greater than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is greater than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is greater than 4096px'
            )
        return value
 
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_upvote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            upvote = Upvote.objects.filter(
                owner=user, post=obj
            ).first()
            return upvote.id if upvote else None
        return None
    
    def get_downvote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            downvote = Downvote.objects.filter(
                owner=user, post=obj
            ).first()
            return downvote.id if downvote else None
        return None

    class Meta:
        model = Post
        fields = [
        'id', 'owner', 'is_owner', 'profile_id', 'location',
         'profile_image', 'make', 'model','year', 'description',
          'image', 'body_types', 'created_at', 'updated_at',
           'upvote_id', 'downvote_id', 'upvotes_count',
            'downvotes_count', 'reviews_count'
        ]