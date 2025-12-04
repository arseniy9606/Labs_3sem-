import unittest
import math

from lab2_oop.rectangle import Rectangle
from lab2_oop.circle import Circle
from lab2_oop.square import Square


class TestFigures(unittest.TestCase):
    def test_rectangle_area(self):
        rect = Rectangle(3, 4, "синий")
        self.assertEqual(rect.area(), 12)

    def test_circle_area(self):
        circle = Circle(2, "зеленый")
        expected = math.pi * 4
        self.assertAlmostEqual(circle.area(), expected, places=5)

    def test_square_area(self):
        square = Square(5, "красный")
        self.assertEqual(square.area(), 25)

    def test_inheritance(self):
        square = Square(5, "красный")
        self.assertTrue(hasattr(square, "width"))
        self.assertTrue(hasattr(square, "height"))
        self.assertEqual(square.width, square.height)


if __name__ == "__main__":
    unittest.main()
