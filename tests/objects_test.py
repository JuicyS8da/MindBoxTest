import unittest
from objects.shapes import Circle, Triangle

class TestCircle(unittest.TestCase):

    def test_circle(self):
        # Test values
        self.assertEqual(Circle(6).calc_square(), 113.09733552923255)
        self.assertEqual(Circle(3).calc_square(), 28.274333882308138)
        self.assertEqual(Circle(15).calc_square(), 706.8583470577034)

    def test_triangle(self):
        # Test values
        self.assertEqual(Triangle(3, 4, 5).calc_square(), 6.0)
        self.assertEqual(Triangle(5, 6, 7).calc_square(), 14.696938456699069)
        self.assertEqual(Triangle(4, 10, 9).calc_square(), 17.984368212422698)

        # Test right triangle
        self.assertEqual(Triangle(3, 4, 5).is_right_triangle(), True)
        self.assertEqual(Triangle(5, 10, 6).is_right_triangle(), False)
        self.assertEqual(Triangle(5, 12, 13).is_right_triangle(), True)

        # Test triangle creation
        with self.assertRaises(ValueError):
            Triangle(1, 1, 70)
            Triangle(2, 2, 8)

if __name__ == '__main__':
    unittest.main()