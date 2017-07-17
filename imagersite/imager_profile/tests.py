from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse_lazy
import factory
import os


class ProfilePageTests(TestCase):

    def setup(self):
        self.client = Client()
        self.user = User(username='flergtheblerg', email='flerg@blerg.com')
        self.user.set_password()
        self.user.save()

    def test_users_profile_info_on_profile_page(self):
        self.clientforce_login(self.user)
        resp = self.client.get(reverse_lazy('imager_profile:profile'))
        self.assertTrue(self.user.username.encode('utf8') in resp.content)
        self.assertTrue(b'<p>Social Status: </p>' in resp.content)
        self.assertTrue(b'<p>Albums: 0 (Public)' in resp.content)
        self.assertTrue(b'<p>Photos: 0 (Public)' in resp.content)
        self.assertTrue(b'<p>No albums yet</p>' in resp.content)

    def test_users_profile_page_has_link_to_library_page(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse_lazy('imager_profile:profile'))
        self.assertTrue(bytes(reverse_lazy('imager_images:library').encode('utf8')) in resp.content)

    def test_when_user_logs_in_redirect_to_profile_page(self):
        resp = self.client.post(reverse_lazy('login'), {
            'username': self.user.username, 'password': 'potatosalad'
        })
        self.assertTrue(resp.url == reverse_lazy('imager_profile:profile'))
