from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


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
        
    # def test_logged_in_user_can_create_post(self):
    #     post_data = {
    #         'make': 'Mazda',
    #         'model': 's-55',
    #         'year': 2000,
    #         'description': 'I really enjoyed it',
    #     }
    #     post_data['image'] = "https://res.cloudinary.com/dwhb1z4jd/image/upload/v1/media/../default_profile_vpfbb8"

    #     self.client.login(username='ada', password='pass')
    #     response = self.client.post('/posts/', post_data)
    #     print(response.status_code)
    #     print(response.content)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     count = Post.objects.count()
    #     self.assertEqual(count, 1)
        








