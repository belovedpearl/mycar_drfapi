from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from posts.models import Post
from upvotes.models import Upvote


class UpvoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
             username='OlaIya', password='Ola123')
        self.post = Post.objects.create(
            owner=self.user,
            make='Make',
            model='Model',
            year=2022,
            description='A lovely time',
            body_types='SUV'
        )

    def test_create_upvote(self):
        upvote = Upvote.objects.create(owner=self.user, post=self.post)
        self.assertEqual(upvote.owner, self.user)
        self.assertEqual(upvote.post, self.post)

    def test_upvote_str_method(self):
        upvote = Upvote.objects.create(owner=self.user, post=self.post)
        resulting_str = f'Upvote - Post: {self.post.make} {self.post.model}'

        self.assertEqual(str(upvote), resulting_str)

    def test_unique_together_constraint(self):
        Upvote.objects.create(owner=self.user, post=self.post)
        # Try creating another upvote with the same owner and post
        with self.assertRaises(Exception):
            Upvote.objects.create(owner=self.user, post=self.post)
