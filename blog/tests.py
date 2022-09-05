from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post


class TestPost(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post1',
            text='this is post1',
            author=cls.user,
            status=Post.STATUS_CHOICES[0][0],
        )
        cls.post2 = Post.objects.create(
            title='Post2',
            text='this is post2',
            author=cls.user,
            status=Post.STATUS_CHOICES[1][0],
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'Post1')
        self.assertEqual(self.post1.text, 'this is post1')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_details_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_title(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_details_by_name(self):
        response = self.client.get(reverse('post_details', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_title(self):
        response = self.client.get(reverse('post_details', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_details_get_404_if_not_exist(self):
        response = self.client.get(reverse('post_details', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'some title',
            'text': 'this is some text',
            'status': 'pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'this is some text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'some title2',
            'text': 'this is some text2',
            'status': 'pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title2')
        self.assertEqual(Post.objects.last().text, 'this is some text2')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id]),)
        self.assertEqual(response.status_code, 302)
