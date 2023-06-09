import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(35000, 0)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = CapuletEngine(35, 0)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_needs_service(self):
        engine = WilloughbyEngine(65000, 0)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = WilloughbyEngine(35, 0)
        self.assertFalse(engine.needs_service())


class TestSterman(unittest.TestCase):
    def test_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())
