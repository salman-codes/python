import unittest
def f1(x):
    return x + 1

class TestMe(unittest.TestCase):
    def test_case(self):
        self.assertEqual(f1(3), 4)

if __name__ == '__main__':
    unittest.main()