import unittest

def add(x,y):
    return x + y

def test_add():
    assert add(1,1) == 2


testcase = unittest.FunctionTestCase(test_add,
                                     setUp=lambda: print('setUp'),
                                     tearDown=lambda: print('tearDown')
)

if __name__ == '__main__':
    unittest.main()
