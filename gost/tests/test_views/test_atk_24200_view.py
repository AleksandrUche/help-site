from django.test import TestCase
from django.urls import reverse


class Atk24200ViewTest(TestCase):
    """Тесты для view заглушки АТК 24.200.02-90 (обычные)"""
    url = reverse('atk24200')
    fixtures = ['gost_data.json']
    data = {
        'execution': '1',
        'pn': '4',
        'dn_passage': '50',
    }

    def test_get_atk_24200_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'АТК 24.200.02-90')
        self.assertTemplateUsed(response, 'gost/atk24200FlangeStoppers.html')

    def test_post_atk_24200_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Масса')
        self.assertContains(response, 'Исполнение заглушки "1"')
