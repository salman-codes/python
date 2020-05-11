import unittest

def mul(data):
	res = 1
	for i in data:
		res = i*res
	return res


class TestSum(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul([3, 3]), 9, "9")

    def test_multiply_tuple(self):
        self.assertEqual(mul((20, 10)), 300, "300")

if __name__ == '__main__':
    unittest.main()