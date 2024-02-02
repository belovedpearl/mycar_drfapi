from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import PostSerializer


class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Setup function
        """
        User.objects.create_user(username='ada', password='pass')

    def test_can_list_post(self):
        """
        Creates a post owner with data
        Checks for successful response
        """
        post_data = {
            'make': 'Mazda',
            'model': 's-55',
            'year': 2000,
            'description': 'I really enjoyed it',
        }
        ada = User.objects.get(username='ada')
        Post.objects.create(owner=ada, **post_data)
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        ada = User.objects.create_user(username='ada', password='pass')
        ife = User.objects.create_user(username='ife', password='word')

        post_data = {
            'make': 'Mazda',
            'model': 's-55',
            'year': 2000,
            'description': 'I really enjoyed it',
        }
        ada = User.objects.get(username='ada')
        Post.objects.create(owner=ada, **post_data)
        post_data = {
            'make': 'Volvo',
            'model': 'w-208',
            'year': 2010,
            'description': 'I really enjoyed it',
        }
        ife = User.objects.get(username='ife')
        Post.objects.create(owner=ife, **post_data)

    def test_can_retrieve_posts_using_valid_id(self):
        response = self.client.get('/posts/2/')
        self.assertEqual(response.data['make'], 'Volvo')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_posts_using_invalid_id(self):
        response = self.client.get('/posts/y/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_users_can_update_their_posts(self):
        self.client.login(username='ada', password='pass')
        response = self.client.patch('/posts/1/', {'make': 'Mercedes'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.make, 'Mercedes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_cannot_update_other_users_posts(self):
        self.client.login(username='ada', password='pass')
        response = self.client.put('/posts/2/', {'make': 'Volvo'})
        post = Post.objects.filter(pk=2).first()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
