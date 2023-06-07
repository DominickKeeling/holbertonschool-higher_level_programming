#!/usr/bin/python3
""" This module is a unittest for the Rectangle class """

import unittest
from unittest.mock import patch
import sys
import io
import json
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""
    def setUp(self):
        """Set up test method"""
        print("Rectangle setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.rectangle = Rectangle(1, 1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0
        # print(f"Base.__nb_objects after reset: {Base._Base__nb_objects}")

    def tearDown(self):
        """Tear down test method"""
        print("Rectangle tearDown")

        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    # test id assignment and if it increments correctly
    def test_id(self):
        """Test __init__ method:
        id assignment in the Rectangle class.
        """
        print(f"Actual id: {self.rectangle.id}")
        self.assertEqual(self.rectangle.id, 1)
        rectangle2 = Rectangle(50, 50)
        print(f"Actual id: {rectangle2.id}")
        self.assertEqual(rectangle2.id, 1)
        rectangle3 = Rectangle(1, 1)
        print(f"Actual id: {rectangle3.id}")
        self.assertEqual(rectangle3.id, 2)
    def test_init(self):
        """Test the initialization of the Rectangle object"""
        r = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 100)

        with self.assertRaises(TypeError):
            Rectangle("10", 20, 1, 2, 100)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 1, 2, 100)

    def test_width(self):
        """Test the width property of Rectangle"""
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        r.width = 30
        self.assertEqual(r.width, 30)
        with self.assertRaises(TypeError):
            r.width = "30"
        with self.assertRaises(ValueError):
            r.width = -30

    def test_height(self):
        """Test the height property of Rectangle"""
        r = Rectangle(10, 20)
        self.assertEqual(r.height, 20)
        r.height = 30
        self.assertEqual(r.height, 30)
        with self.assertRaises(TypeError):
            r.height = "30"
        with self.assertRaises(ValueError):
            r.height = -30

    def test_x(self):
        """Test the x property of Rectangle"""
        r = Rectangle(10, 20, 1, 2)
        self.assertEqual(r.x, 1)
        r.x = 5
        self.assertEqual(r.x, 5)
        with self.assertRaises(TypeError):
            r.x = "5"
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y(self):
        """Test the y property of Rectangle"""
        r = Rectangle(10, 20, 1, 2)
        self.assertEqual(r.y, 2)
        r.y = 5
        self.assertEqual(r.y, 5)
        with self.assertRaises(TypeError):
            r.y = "5"
        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        """Test the area method of Rectangle"""
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        """Test the display method of Rectangle"""
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with io.StringIO() as buf, patch("sys.stdout", buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, expected_output)

    def test_str(self):
        """Test the string representation of Rectangle"""
        r = Rectangle(10, 20, 1, 2, 100)
        expected_str = "[Rectangle] (100) 1/2 - 10/20"
        self.assertEqual(str(r), expected_str)
    
    class TestRectangle(unittest.TestCase):

    def test_update_args(self):
        """Test the update method of Rectangle with args"""
        r = Rectangle(10, 20, 1, 2, 100)
        r.update(50, 30, 3, 4, 200)
        self.assertEqual(str(r), "[Rectangle] (50) 3/4 - 30/20")

    def test_update_kwargs(self):
        """Test the update method of Rectangle with kwargs"""
        r = Rectangle(10, 20, 1, 2, 100)
        r.update(id=50, width=30, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (50) 3/4 - 30/20")

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle"""
        r = Rectangle(10, 20, 1, 2, 100)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 100, 'width': 10, 'height': 20, 'x': 1, \
                                                                   'y': 2})
        self.assertIsInstance(d, dict)

    def test_save_to_file(self):
        """Test the save_to_file class method of Rectangle"""
        r1 = Rectangle(10, 20, 1, 2, 100)
        r2 = Rectangle(5, 10, 0, 0, 200)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(json.loads(data), [{'width': 10, 'height': 20, \
                                                              'x': 1, 'y': 2, \
                                                              'id': 100}, \
                                                {'width': 5, 'height': 10, \
                                                 'x': 0, 'y': 0, 'id': 200}])

    def test_save_to_file_empty(self):
        """Test the save_to_file class method with an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_none(self):
        """Test the save_to_file class method with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_load_from_file(self):
        """Test the load_from_file class method of Rectangle"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertFalse(os.path.exists("Rectangle.json"))
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])
        r1 = Rectangle(10, 20, 1, 2, 100)
        r2 = Rectangle(5, 10, 0, 0, 200)
        Rectangle.save_to_file([r1, r2])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 2)
        self.assertIsInstance(list_objs[0], Rectangle)
        self.assertIsInstance(list_objs[1], Rectangle)
        self.assertEqual(str(list_objs[0]), "[Rectangle] (100) 1/2 - 10/20")
        self.assertEqual(str(list_objs[1]), "[Rectangle] (200) 0/0 - 5/10")


if __name__ == '__main__':
    unittest.main()
