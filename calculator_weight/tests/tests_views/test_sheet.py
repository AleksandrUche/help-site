from django.test import TestCase
from django.urls import reverse


class SheetViewTest(TestCase):
    """Лист"""
    url = reverse('sheet')
    data = {
        'side_a': '600',
        'side_b': '600',
        'thickness': '16',
        'material': '7850',
    }

    def test_sheet_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Лист')
        self.assertTemplateUsed(response, 'calculator_weight/sheet.html')

    def test_ajax_get_sheet_view(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '45.216'}
        self.assertEqual(response.json(), expected_data)
