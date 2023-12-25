from django.test import TestCase
from django.urls import reverse


class Gost33259ViewTest(TestCase):
    """Тесты для view фланцев ГОСТ 33259-2015"""
    url = reverse('gost33259')
    fixtures = ['gost_data.json']
    data = {
        'type_fl': '01',
        'surface': 'E',
        'dn_passage': '40',
        'pn': '10',
        'row': '1',
    }

    def test_get_gost_33259_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ГОСТ 33259-2015')
        self.assertTemplateUsed(response, 'gost/gost_33259_flange.html')

    def test_post_gost_33259_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Масса фланца: 1,72 кг')
