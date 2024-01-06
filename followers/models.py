from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'followed'
    'owner' is a User following another User
    'followed' is a User that is followed by 'owner'
    related_name is a required attribute for easy differentiation
    between 'owner' and 'followed'
    ordered in descending order of creation
    'unique_together' ensures a user can't follow' the same user more than once
    """

    owner = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User, related_name="followed", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "followed"]

    def __str__(self):
        return f"{self.owner.username} follows {self.followed.username}"