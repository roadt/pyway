

import unittest
from six import print_

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEqual((1+2), 3)
        self.assertEqual(0+1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


class Case1(unittest.TestCase):
    
    def setUp(self):
        print_('setUp')

    def tearDown(self):
        print_('tearDown')


    def test1(self):
        print_("test1")

    def test2(self):
        print_("test2")


if __name__ == '__main__':
    unittest.main()


