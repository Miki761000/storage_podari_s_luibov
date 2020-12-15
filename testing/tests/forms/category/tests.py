from django.test import TestCase
from django.urls import reverse

from warehouse.models import Category


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

    # def test_getting_delete_view(self):
    #     category = Category.objects.get(category_name='test')
    #
    #     response = self.client.get(reverse('delete category', args=(category.id,)), follow=True)
    #     # self.assertContains(response, 'Are you sure you want to delete')
    #     self.client.post(reverse('delete category', args=(category.id,)), follow=True)
    #     self.assertRedirects(response, reverse('list category'), status_code=302)

    # def test_get_absolute_url(self):
    #     response = self.client.get('/list_category/')
    #     self.assertEqual(response.status_code, 200)

