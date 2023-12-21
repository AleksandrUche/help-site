from django.test import TestCase
from django.urls import reverse


class GetAjaxFormValuesGost33259Test(TestCase):
    url = reverse('get_values_gost_33259')
    fixtures = ['gost_data.json']
    data_type_fl = {'01': {'type_fl': '01'}, '02': {'type_fl': '02'}, '11': {'type_fl': '11'}}
    data_type_and_pn_fl = {
        '01': {'type_fl': '01', 'dn_passage': '50'},
        '02': {'type_fl': '02', 'dn_passage': '50'},
        '11': {'type_fl': '11', 'dn_passage': '50'}
    }

    def test_type_01_get_dn_passage_option(self):
        expected_data = {
            'dn_passage_option': [10, 15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 350, 400, 450,
                                  500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400]
        }
        response = self.client.get(self.url, self.data_type_fl['01'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_type_02_get_dn_passage_option(self):
        expected_data = {
            'dn_passage_option': [10, 15, 20, 25, 32, 40, 50, 65, 80, 100, 125,
                                  150, 200, 250, 300, 350, 400, 450, 500, 600]
        }
        response = self.client.get(self.url, self.data_type_fl['02'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_type_11_get_dn_passage_option(self):
        expected_data = {
            'dn_passage_option': [10, 15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500,
                                  600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000,
                                  3200, 3400, 3600, 3800, 4000]
        }
        response = self.client.get(self.url, self.data_type_fl['11'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_type_01_get_pn_option(self):
        expected_data = {'pn_option': [1.0, 2.5, 6.0, 10.0, 16.0, 25.0]}
        response = self.client.get(self.url, self.data_type_and_pn_fl['01'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_type_02_get_pn_option(self):
        expected_data = {'pn_option': [1.0, 2.5, 6.0, 10.0, 16.0, 25.0]}
        response = self.client.get(self.url, self.data_type_and_pn_fl['02'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_type_11_get_pn_option(self):
        expected_data = {'pn_option': [1.0, 2.5, 6.0, 10.0, 16.0, 25.0, 40.0, 63.0, 100.0, 160.0, 50.0, 200.0, 250.0]}
        response = self.client.get(self.url, self.data_type_and_pn_fl['11'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
