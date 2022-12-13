import unittest
from unittest import TestCase

from .scripts.InsertJson import *

class TestMovie(TestCase):

    def test_sum(self):
        data = convertToJson()
        self.assertEqual(data[0]['title'], "Stranger Things")


if __name__ == "__main__":
    unittest.main()