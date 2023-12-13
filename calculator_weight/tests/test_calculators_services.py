from django.test import TestCase
from calculator_weight.services.calculators_services import *


class CalculatorsServicesTest(TestCase):

    def test_round_the_number(self):
        rounding_1 = round_the_number(Decimal('1.0000'), '1.000')
        rounding_2 = round_the_number(Decimal('1.0000'), '1.00')
        rounding_3 = round_the_number(Decimal('1.0000'), '1.0')
        rounding_4 = round_the_number(Decimal('1.0000'), '1')
        rounding_5 = round_the_number(Decimal('1.0000'))
        self.assertEqual(rounding_1, Decimal('1.000'))
        self.assertEqual(rounding_2, Decimal('1.00'))
        self.assertEqual(rounding_3, Decimal('1.0'))
        self.assertEqual(rounding_4, Decimal('1'))
        self.assertEqual(rounding_5, Decimal('1.000'))

    def test_calculate_mass_corner_equal(self):
        result = calculate_mass_corner_equal(
            side=Decimal(50),
            thickness=Decimal(5),
            length=Decimal(1),
            material='7850',
        )
        self.assertEqual(result, Decimal('3.729'))

    def test_calculate_mass_corner_different(self):
        result = calculate_mass_corner_different(
            side=Decimal(50),
            side_b=Decimal(60),
            thickness=Decimal(5),
            length=Decimal(1),
            material='7850',
        )
        self.assertEqual(result, Decimal('4.121'))

    def test_calculate_mass_circle(self):
        result = calculate_mass_circle(
            diameter=Decimal(12),
            length=Decimal(1),
            material='7850',
        )
        self.assertEqual(result, Decimal('0.888'))

    def test_calculate_mass_square(self):
        result = calculate_mass_square(
            size=Decimal(20),
            length=Decimal(1),
            material='7850',
        )
        self.assertEqual(result, Decimal('3.140'))

    def test_calculate_mass_sheet(self):
        result = calculate_mass_sheet(
            side_a=Decimal(300),
            side_b=Decimal(500),
            thickness=Decimal(16),
            material='7850',
        )
        self.assertEqual(result, Decimal('18.840'))

    def test_calculate_mass_tube(self):
        result = calculate_mass_tube(
            diameter=Decimal(300),
            thickness=Decimal(16),
            length=Decimal(1),
            material='7850',
        )
        self.assertEqual(result, Decimal('112.062'))

    def test_calculate_mass_profile_pipe(self):
        result = calculate_mass_profile_pipe(
            side_a=Decimal(300),
            side_b=Decimal(500),
            thickness=Decimal(16),
            length=Decimal(1),
            material='7850',
        )
        self.assertEqual(result, Decimal('189.465'))
