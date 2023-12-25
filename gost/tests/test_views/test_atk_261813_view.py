from django.test import TestCase
from django.urls import reverse


class Atk261813ViewTest(TestCase):
    """Тесты для view фланцев АТК 26-18-13-96"""
    url = reverse('atk261813')
    fixtures = ['gost_data.json']
    data = {
        'execution': '1',
        'pn': '4',
        'dn_passage': '50',
    }

    def test_get_atk_261813_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'АТК 26-18-13-96')
        self.assertTemplateUsed(response, 'gost/atk261813.html')

    def test_post_atk_261813_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Масса')
        self.assertContains(response, 'Исполнение фланца: "1"')
