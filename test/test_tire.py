import unittest
from tire.carrigan_tire import CarriganTire
from tire.octaprime_tire import OctaPrimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_servicing(self):
        tires = CarriganTire(0.95, 0.1, 0.2, 0.5)
        self.assertTrue(tires.needs_service())

    def test_does_not_need_servicing(self):
        tires = CarriganTire(0.2, 0.3, 0.4, 0.1)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_servicing(self):
        tires = OctaPrimeTire(0.95, 0.9, 0.8, 0.7)
        self.assertTrue(tires.needs_service())

    def test_does_not_need_servicing(self):
        tires = OctaPrimeTire(0.2, 0.3, 0.4, 0.1)
        self.assertFalse(tires.needs_service())
