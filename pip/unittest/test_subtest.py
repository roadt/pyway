import unittest


class NumbersTests(unittest.TestCase):
  
  
    def test_even_subtests(self):
        ''' test number between 0 and 5 are all even '''
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i%2, 0)

    def test_even(self):
        ''' test number between 0 and 5 are all even '''
        for i in range(0, 6):
            self.assertEqual(i%2, 0)



if __name__ == '__main__':
    unittest.main()
