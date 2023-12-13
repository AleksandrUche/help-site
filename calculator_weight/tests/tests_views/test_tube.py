from django.test import TestCase
from django.urls import reverse


class TubeViewTest(TestCase):
    """Трубы"""
    url = reverse('tube')
    data = {
        'diameter': '57',
        'thickness': '6',
        'length': '1',
        'material': '7850',
    }

    def test_tube_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Труба')
        self.assertTemplateUsed(response, 'calculator_weight/tube.html')

    def test_ajax_get_tube_view(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '7.546'}
        self.assertEqual(response.json(), expected_data)
