from django.test import TestCase
from django.urls import reverse


class ProfilePipeViewTest(TestCase):
    """Профильная труба"""
    url = reverse('profile_pipe')
    data = {
        'side_a': '40',
        'side_b': '20',
        'thickness': '2',
        'length': '1',
        'material': '7850',
    }

    def test_profile_pipe_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Профильная труба')
        self.assertTemplateUsed(response, 'calculator_weight/profile_pipe.html')

    def test_ajax_get_profile_pipe_view(self):
        """AJAX GET"""
        response = self.client.get(
            self.url,
            self.data,
        )
        self.assertEqual(response.status_code, 200)
        expected_data = {'weight': '1.704'}
        self.assertEqual(response.json(), expected_data)
