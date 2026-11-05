import unittest
import p4

class MyTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(p4.sum(3, 3),3)

    def test_mul(self):
        self.assertEqual(p4.mul(1, 120), 20)

    def test_div(self):
        self.assertEqual(p4.div(6, 2), 3)
        self.assertRaises(ZeroDivisionError, p4.div, 12, 0)
if __name__ == '__main__':
    unittest.main()
