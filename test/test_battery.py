import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbin(unittest.TestCase):
    def test_needs_service(self):
        battery = NubbinBattery(datetime.today().date().replace(
            year=2017), datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        battery = NubbinBattery(datetime.today().date(),
                                datetime.today().date())
        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):
    def test_needs_service(self):
        battery = SpindlerBattery(datetime.today().date().replace(
            year=2019), datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        battery = SpindlerBattery(
            datetime.today().date(), datetime.today().date())
        self.assertFalse(battery.needs_service())
