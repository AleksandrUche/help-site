from django.test import TestCase
from django.urls import reverse


class Gost6533FlangeStoppersViewTest(TestCase):
    """Тесты для view днища по ГОСТ 6533-78"""
    url = reverse('gost6533')
    fixtures = ['gost_data.json']
    data = {
        'drawing': '2',
        'diameter': '3400',
        'thickness': '16',
    }

    def test_get_gost_6533_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ГОСТ 6533-78')
        self.assertTemplateUsed(response, 'gost/gost_6533_bottom.html')

    def test_post_gost_6533_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1673,4')
        self.assertContains(response, 'Чертеж "2"')
