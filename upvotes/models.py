from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Upvote(models.Model):
    """
    Upvote model which relates to owner and post
    Orders in descending order of time creation
    unique-together restricts users from submiting more votes for the same post
    returns a string containing the make and model for easy recognition
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='upvotes', on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'Upvote - Post: {self.post.make} {self.post.model}'
