from django.test import TestCase
from django.urls import reverse


class BasicPageGostTest(TestCase):
    url = reverse('documents')

    def test_basic_page_gost_view(self):
        """Начальная страница отображения всех стандартов"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Фланцы')
        self.assertContains(response, 'Заглушки')
        self.assertContains(response, 'Днища')
        self.assertTemplateUsed(response, 'gost/documents.html')
