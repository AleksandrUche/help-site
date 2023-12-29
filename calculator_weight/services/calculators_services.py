import math
from decimal import Decimal


def round_the_number(meaning: Decimal, rounding='1.000') -> Decimal:
    """Округляет Decimal число"""
    return meaning.quantize(Decimal(rounding))


def calculate_mass_corner_equal(side: Decimal,
                                thickness: Decimal,
                                length: Decimal,
                                material: str) -> Decimal:
    """Расчет массы уголка равнополочного"""
    calculation_weight = \
        (side / 1000 * 2 - thickness / 1000) * thickness / 1000 * length * Decimal(material)
    return round_the_number(calculation_weight)


def calculate_mass_corner_different(side: Decimal,
                                    side_b: Decimal,
                                    thickness: Decimal,
                                    length: Decimal,
                                    material: str) -> Decimal:
    """Расчет массы уголка с разными полками"""
    calculation_weight = \
        (side / 1000 + side_b / 1000 - thickness / 1000) * thickness / 1000 * length * Decimal(material)
    return round_the_number(calculation_weight)


def calculate_mass_circle(diameter: Decimal, length: Decimal, material: str) -> Decimal:
    """Расчет массы круга"""
    calculation_weight = Decimal(math.pi) / 4 * Decimal(material) * (diameter / 1000) ** 2 * length
    return round_the_number(calculation_weight)


def calculate_mass_square(size: Decimal, length: Decimal, material: str) -> Decimal:
    """Расчет массы квадрата"""
    calculation_weight = Decimal(material) * (size / 1000) ** 2 * length
    return round_the_number(calculation_weight)


def calculate_mass_sheet(side_a: Decimal, side_b: Decimal, thickness: Decimal, material: str) -> Decimal:
    """Расчет массы листа"""
    calculation_weight = side_a / 1000 * side_b / 1000 * thickness / 1000 * Decimal(material)
    return round_the_number(calculation_weight)


def calculate_mass_tube(diameter: Decimal, thickness: Decimal, length: Decimal, material: str) -> Decimal:
    """Расчет массы трубы"""
    # Внутренний диаметр
    inner_diameter = diameter / 1000 - 2 * thickness / 1000
    # Площадь
    square = Decimal(math.pi) / 4 * ((diameter / 1000) ** 2 - inner_diameter ** 2)
    # Расчет массы листа
    calculation_weight = square * length * Decimal(material)
    return round_the_number(calculation_weight)


def calculate_mass_profile_pipe(side_a: Decimal,
                                side_b: Decimal,
                                thickness: Decimal,
                                length: Decimal,
                                material: str) -> Decimal:
    """Расчет массы профильной трубы"""
    calculation_weight = (Decimal(material) / Decimal(7850) * Decimal('0.0157') * thickness * (
                          side_a + side_b - Decimal('2.86') * thickness)) * length
    return round_the_number(calculation_weight)


def calculate_mass_of_reference_values(mass_channel: float, length: Decimal) -> Decimal:
    """Расчет массы по значениям из БД (справочные значения)"""
    calculation_weight = Decimal(mass_channel) * length
    return round_the_number(calculation_weight)
