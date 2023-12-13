from django.test import TestCase
from django.urls import reverse


class CalculatorViewTest(TestCase):
    """Уголок неравнополочный"""
    url = reverse('corner_different')
    data = {
        'side': '50',
        'side_b': '60',
        'thickness': '5',
        'length': '1',
        'material': '7850',
    }

    def test_corner_different_shelves_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Уголок неравнополочный')
        self.assertTemplateUsed(response, 'calculator_weight/corner_different_shelves.html')

    def test_ajax_get_different_shelves_view(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '4.121'}
        self.assertEqual(response.json(), expected_data)
