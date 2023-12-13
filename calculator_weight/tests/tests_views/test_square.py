from django.test import TestCase
from django.urls import reverse


class SquareViewTest(TestCase):
    """Квадрат"""
    url = reverse('square')
    data = {
        'size': '20',
        'length': '1',
        'material': '7850',
    }

    def test_square_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Квадрат')
        self.assertTemplateUsed(response, 'calculator_weight/square.html')

    def test_ajax_get_square_view(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '3.140'}
        self.assertEqual(response.json(), expected_data)
