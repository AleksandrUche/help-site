from django.test import TestCase
from django.urls import reverse


class GetAjaxFormValuesGost6533Test(TestCase):
    url = reverse('get_values_gost_6533')
    fixtures = ['gost_data.json']
    data_drawing = {'drawing': '1'}
    data_drawing_and_diameter = {'drawing': '1', 'diameter': '3400'}

    def test_get_diameter_option(self):
        expected_data = {
            'diameter_option': [133, 159, 168, 219, 273, 325, 377, 426, 480, 530,
                                630, 720, 820, 920, 1020, 1120, 1220, 1320, 1420]
        }
        response = self.client.get(self.url, self.data_drawing)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_get_thickness_option(self):
        expected_data = {
            'thickness_option':
                ["12", "14", "16", "18", "20", "22", "25", "28", "30", "32", "34", "36", "38", "40", "45", "50", "55",
                 "60", "65", "70", "80", "90", "100", "110", "120", "10", "12", "14", "16", "20"]
        }
        response = self.client.get(self.url, self.data_drawing_and_diameter)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
