import unittest

def sample_func1(a,b):
    return a+b

def sample_func2(a,b):
    return a+b

def sample_func3(a):
    if(a>5):
        return True

class Test(unittest.TestCase):
    def test_sample_func1(self):
        self.assertEqual(sample_func1(5,3),8)
        
    def test_sample_func2(self):
        self.assertEqual(sample_func2(5,3),2)

    def test_sample_func3(self):
        self.assertTrue(sample_func3(2))


if __name__ == '__main__':
    unittest.main()
