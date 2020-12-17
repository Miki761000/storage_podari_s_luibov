from django.contrib.auth.models import Group, User
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import UserProfile
from warehouse.models import Category


class NoSuchElementException(object):
    pass


class CategoryTestCase(TestCase):

    def setUp(self):
        name = 'test'
        Category.objects.create(category_name=name)

    def test_add_new_category(self):
        category = Category.objects.get(category_name='test')
        self.assertEqual(category.category_name, 'test')

    def test_count_in_list_categories(self):
        object_list = Category.objects.all()
        self.assertEqual(object_list.count(), 1)

    def test_update_category(self):
        category = Category.objects.get(category_name='test')
        response = self.client.post(
            reverse('edit category', kwargs={'pk': category.id}),
            {'category_name': 'test'})

        self.assertEqual(response.status_code, 302)

        category.refresh_from_db()
        self.assertEqual(category.category_name, 'test')

    def test_changes_in_name_category(self):
        category = Category.objects.get(category_name='test')
        category.category_name = 'test1'
        self.client.post('edit category', data={'category_name': 'test1'})
        self.assertEqual(category.category_name, 'test1')

    def test_delete_request(self):
        category = Category.objects.get(category_name='test')
        c = Client()
        c.login(username='admin', password='admin')
        response = self.client.get(reverse('delete category', args=(category.id,)), follow=True)
        self.assertEqual(200, response.status_code)
        post_response = self.client.post(reverse('delete category', args=(category.id,)), follow=True)
        self.assertEqual(200, post_response.status_code)

    def test_login(self):
        c = Client()
        response = c.post('/login/', {'username': 'admin', 'password': 'admin'})
        response.status_code

