import unittest2
import text_pyramid
from unittest2.case import skip


class TestTextPyramid(unittest2.TestCase):
    def test_should_return_list_of_strings(self):
        pyramid = text_pyramid.get_strings('a')
        self.assertEqual(pyramid, ['a'])

    def test_should_return_pyramid_if_lowercase(self):
        pyramid = text_pyramid.get_strings('apple')
        expected_pyramid = [
            'a',
            'ap',
            'app',
            'appl',
            'apple',
            'appl',
            'app',
            'ap',
            'a',
        ]
        self.assertEqual(pyramid, expected_pyramid)
