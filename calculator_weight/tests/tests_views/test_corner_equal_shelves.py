from django.test import TestCase
from django.urls import reverse


class CornerEqualShelvesTest(TestCase):
    """Уголок равнополочный"""
    url = reverse('corner_equal')
    data = {
        'side': '50',
        'thickness': '5',
        'length': '1',
        'material': '7850',
    }

    def test_corner_equal_shelves_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Уголок равнополочный')
        self.assertTemplateUsed(response, 'calculator_weight/corner_equal_shelves.html')

    def test_ajax_get_corner_equal_shelves(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '3.729'}
        self.assertEqual(response.json(), expected_data)
