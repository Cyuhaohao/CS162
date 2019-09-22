import unittest
from CS162_4 import ClockIterator

class TestClock(unittest.TestCase):

    def setUp(self):
        print("Clear the environment.")

    def test_values(self):

        clock = ClockIterator()
        a=next(clock)
        self.assertEqual("00:00",a)

        for i in range(58):
            next(clock)
        a = next(clock)
        self.assertEqual("00:59",a)

        a = next(clock)
        self.assertEqual("01:00",a)

        for i in range(1378):
            next(clock)
        a = next(clock)
        self.assertEqual("23:59",a)

        a = next(clock)
        self.assertEqual("00:00",a)

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestClock))
    unittest.main()
