import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import io
import sys
import os
from contextlib import redirect_stdout
import json


"""
Unit test for the size, setter, getter, update and dictionary methods of the square
"""

class TestSquare(unittest.TestCase):
    """ test for size and everything """

    @classmethod
    def setUp(self):
        """Set up test method"""
        # reset __nb_objects to 0 before each test
        print("Square setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.square = Square(1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down test method """
        print("Square tearDown")

        sys.stdout = sys.__stdout__

        del self.square
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_square_inheritance(self):
        """ Test if Square inherits from Rectangle """
        self.assertIsInstance(self.square, Rectangle)

    def test_square_inheritance_base(self):
        """ Test if Square inherits from Base """
        self.assertIsInstance(self.square, Base)


    def test_id(self):
        """ Test if Square id is assigned correctly """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

     def test_square_id_assignment(self):
        """ Test if Square id is assigned correctly """
        # Test explicit id assignment positive number
        square4 = Square(6, 0, 0, 12)
        self.assertEqual(square4.id, 12)

        # Test auto-increment id after explicit assignment
        square5 = Square(5, 0, 0, None)
        self.assertEqual(square5.id, 1)

        # Test explicit id assignment with negative number
        square6 = Square(4, 0, 0, -12)
        self.assertEqual(square6.id, -12)

        # Test explicit id assignment with zero
        square7 = Square(5, 0, 0, 0)
        self.assertEqual(square7.id, 0)

    def test_size(self):
        """ Test if created correctly """
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_x(self):
        """ Test if x works """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_size_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_size_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_value_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_value_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            self.s1.area(1)

    def test_basic_display(self):
        s = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, "###\n")

    def test_create_instance(self):
        """Test creating an instance of Square"""
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Base)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_create_instance_with_position(self):
        """Test creating an instance of Square with position"""
        s = Square(5, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_create_instance_with_id(self):
        """Test creating an instance of Square with custom id"""
        s = Square(5, id=10)
        self.assertEqual(s.id, 10)

    def test_create_instance_with_invalid_size(self):
        """Test creating an instance of Square with invalid size"""
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_create_instance_with_invalid_position(self):
        """Test creating an instance of Square with invalid position"""
        with self.assertRaises(ValueError):
            s = Square(5, -2, 3)

    def test_create_instance_with_extra_args(self):
        """Test creating an instance of Square with extra arguments"""
        s = Square(5, 2, 3, 4, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_update_args(self):
        """Test updating attributes using args"""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(10, 2)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 2")
        s.update(10, 2, 3)
        self.assertEqual(str(s), "[Square] (10) 3/0 - 2")
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Test updating attributes using kwargs"""
        s = Square(5)
        s.update(id=10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(size=2)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 2")
        s.update(x=3)
        self.assertEqual(str(s), "[Square] (10) 3/0 - 2")
        s.update(y=4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")
        s.update(id=20, size=5, x=1, y=2)
        self.assertEqual(str(s), "[Square] (20) 1/2 - 5")


    def test_update_kwargs_unknown_key(self):
        """test update with unknown key"""
        s = Square(1, 0, 0, 1)
        s.update(size=10, weight=5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_to_dict(self):
        """Test conversion to dictionary"""
        s = Square(5, 2, 3, 10)
        s_dict = s.to_dictionary()
        self.assertIsInstance(s_dict, dict)
        self.assertEqual(s_dict['id'], 10)
        self.assertEqual(s_dict['size'], 5)
        self.assertEqual(s_dict['x'], 2)
        self.assertEqual(s_dict['y'], 3)

    def test_to_json_string(self):
        """Test conversion to JSON string"""
        s = Square(5, 2, 3, 10)
        s_json = s.to_json_string()
        self.assertIsInstance(s_json, str)
        self.assertEqual(json.loads(s_json), [{"id": 10, "size": 5, "x": 2, "y": 3}])

    def test_from_json_string(self):
        """Test conversion from JSON string"""
        s_json = '[{"id": 10, "size": 5, "x": 2, "y": 3}]'
        s_list = Square.from_json_string(s_json)
        self.assertIsInstance(s_list, list)
        self.assertEqual(len(s_list), 1)
        self.assertEqual(s_list[0].id, 10)
        self.assertEqual(s_list[0].size, 5)
        self.assertEqual(s_list[0].x, 2)
        self.assertEqual(s_list[0].y, 3)

    def test_save_to_file(self):
        """Test the save_to_file class method"""
        s1 = Square(10, 2, 1, 8)
        s2 = Square(2, 0, 0, 9)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(json.loads(data), [{'size': 10, \
            'x': 2, 'id': 8, 'y': 1}, {'size': 2, 'x': 0, 'id': 9, 'y': 0}])

    def test_save_to_file_empty(self):
        """Test the save_to_file class method with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_none(self):
        """Test the save_to_file class method with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_load_from_file(self):
        """Test the load_from_file class method"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertFalse(os.path.exists("Square.json"))
        list_objs = Square.load_from_file()
        self.assertEqual(list_objs, [])
        s1 = Square(10, 2, 1, 8)
        s2 = Square(2, 0, 0, 9)
        Square.save_to_file([s1, s2])
        list_objs = Square.load_from_file()
        self.assertEqual(len(list_objs), 2)
        self.assertIsInstance(list_objs[0], Square)
        self.assertIsInstance(list_objs[1], Square)
        self.assertEqual(str(list_objs[0]), "[Square] (8) 2/1 - 10")
        self.assertEqual(str(list_objs[1]), "[Square] (9) 0/0 - 2")

    
if __name__ == '__main__':
    unittest.main()
