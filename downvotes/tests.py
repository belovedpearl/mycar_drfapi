from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from posts.models import Post
from downvotes.models import Downvote

class DownvoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='OlaIya', password='Ola123')
        self.post = Post.objects.create(
            owner = self.user,
            make = 'Make',
            model = 'Model',
            year = 2022,
            description = 'A lovely time',
            body_types = 'SUV'
        )

    def test_create_downvote(self):
        downvote = Downvote.objects.create(owner = self.user, post = self.post)       
        self.assertEqual(downvote.owner, self.user)
        self.assertEqual(downvote.post, self.post)
    
    def test_downvote_str_method(self):
        downvote = Downvote.objects.create(owner = self.user, post = self.post)
        resulting_str = f'Downvote - Post: {self.post.make} {self.post.model}'
        
        self.assertEqual(str(downvote), resulting_str)

    def test_unique_together_constraint(self):
        Downvote.objects.create(owner=self.user, post=self.post)      
        # Try creating another downvote with the same owner and post
        with self.assertRaises(Exception):
            Downvote.objects.create(owner = self.user, post = self.post)
