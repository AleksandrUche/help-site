from django.test import TestCase
from django.urls import reverse


class GetAjaxFormValuesAtk26185Test(TestCase):
    url = reverse('get_values_atk_26185_flange_stoppers')
    fixtures = ['gost_data.json']
    data_execution = {'execution': '1'}
    data_execution_and_pn = {'execution': '1', 'pn': '4.0'}

    def test_get_pn_option(self):
        expected_data = {'pn_option': [1.6, 2.5, 4.0]}
        response = self.client.get(self.url, self.data_execution)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_get_dn_passage_option(self):
        expected_data = {'dn_passage_option': [25, 50, 80, 100, 150, 200, 250, 300, 350, 400, 500]}
        response = self.client.get(self.url, self.data_execution_and_pn)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
