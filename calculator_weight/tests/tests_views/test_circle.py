from django.test import TestCase
from django.urls import reverse


class CircleViewTest(TestCase):
    """Кругляк"""
    url = reverse('circle')
    data = {
        'diameter': '12',
        'length': '1',
        'material': '7850',
    }

    def test_circle_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Кругляк')
        self.assertTemplateUsed(response, 'calculator_weight/circle.html')

    def test_ajax_get_circle_view(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '0.888'}
        self.assertEqual(response.json(), expected_data)
