from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Review

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='ola',
            password='ade123'
        )
        self.post = Post.objects.create(
            make='Make',
            model='Model',
            year='2000',
            description='Description',
            body_types='SUV',
            owner=self.user
        )

    def test_review_creation(self):
        review = Review.objects.create(
            owner=self.user,
            post=self.post,
            content='Review Content'
        )

        self.assertEqual(review.owner, self.user)
        self.assertEqual(review.post, self.post)
        self.assertEqual(review.content, 'Review Content')

    def test_review_ordering(self):
        review1 = Review.objects.create(
            owner=self.user,
            post=self.post,
            content='Review 1'
        )
        review2 = Review.objects.create(
            owner=self.user,
            post=self.post,
            content='Review 2'
        )

        reviews = Review.objects.all()

        self.assertEqual(reviews.count(), 2)
        self.assertEqual(reviews[0], review2)
        self.assertEqual(reviews[1], review1)

    def test_review_str_representation(self):
        review = Review.objects.create(
            owner=self.user,
            post=self.post,
            content='Review Content'
        )

        expected_str = f"Content: {review.content}"
        self.assertEqual(str(review), expected_str)
