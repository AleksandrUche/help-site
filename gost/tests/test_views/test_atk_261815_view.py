from django.test import TestCase
from django.urls import reverse


class Atk26185FlangeStoppersViewTest(TestCase):
    """Тесты для view заглушки АТК 26-18-5-93 (поворотные)"""
    url = reverse('atk26185')
    fixtures = ['gost_data.json']
    data = {
        'execution': '1',
        'pn': '4',
        'dn_passage': '50',
    }

    def test_get_atk_26185_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'АТК 26-18-5-93')
        self.assertTemplateUsed(response, 'gost/atk2618FlangeStoppers.html')

    def test_post_atk_26185_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Масса')
        self.assertContains(response, 'Исполнение заглушки: "1"')
