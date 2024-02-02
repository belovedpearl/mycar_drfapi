from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Follower


class FollowerTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
             username='ola', password='adeola1')
        self.user2 = User.objects.create_user(
            username='ifeOlu', password='olumide2')
        self.url = '/followers/'

    def test_user_can_follow_another_user(self):
        self.client.login(username='ola', password='adeola1')
        data = {'followed': self.user2.id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.first().owner, self.user1)
        self.assertEqual(Follower.objects.first().followed, self.user2)

    def test_user_can_unfollow_another_user(self):
        follower = Follower.objects.create(
             owner=self.user1, followed=self.user2)
        self.client.login(username='ola', password='adeola1')

        response = self.client.delete(f'/followers/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)

    def test_user_cannot_unfollow_if_not_following(self):
        self.client.login(username='ola', password='adeola1')

        non_existing_follower_id = 123
        response = self.client.delete(
             f'/followers/{non_existing_follower_id}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Follower.objects.count(), 0)
