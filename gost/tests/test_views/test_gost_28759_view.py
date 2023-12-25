from django.test import TestCase
from django.urls import reverse


class Gost28759ViewTest(TestCase):
    """Тесты для view фланцев ГОСТ 28759.3—2022"""
    url = reverse('gost28759')
    fixtures = ['gost_data.json']
    data = {
        'execution': '1',
        'dn_passage': '500',
        'pn': '2.5',
    }

    def test_get_gost_28759_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ГОСТ 28759.3-2022')
        self.assertTemplateUsed(response, 'gost/gost_28759_flange.html')

    def test_post_gost_28759_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Масса фланца: 43,9 кг')
