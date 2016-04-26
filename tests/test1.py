from nose import *
import unittest

class Test1(unittest.TestCase):

    def sample_test(self):
        assert True
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()