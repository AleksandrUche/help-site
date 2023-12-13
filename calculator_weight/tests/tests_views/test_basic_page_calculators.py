from django.test import TestCase
from django.urls import reverse


class BasicPageCalculatorsTest(TestCase):
    url = reverse('calculator_weigh')

    def test_basic_page_calculators_view(self):
        """Начальная страница отображения всех калькуляторов"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Металлопрокат')
        self.assertTemplateUsed(response, 'calculator_weight/all_calculator_weight.html')
