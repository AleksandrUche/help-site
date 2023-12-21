from django.test import TestCase
from django.urls import reverse


class GetAjaxFormValuesGost33259Test(TestCase):
    url = reverse('get_values_gost_28759')
    fixtures = ['gost_data.json']
    data_dn_passage = {'dn_passage': '800'}

    def test_get_dn_passage_option(self):
        expected_data = {
            'pn_option': [1.0, 1.6, 2.5, 4.0, 6.3]
        }
        response = self.client.get(self.url, self.data_dn_passage)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
