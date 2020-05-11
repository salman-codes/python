import unittest
class AlmostEqualTest(unittest.TestCase):

	def testAlmostEqual(self):
		self.assertAlmostEqual(1.1, 3.3 - 2.2, places=1)

	def testGreaterEqual(self):
		self.assertGreaterEqual(21, 12, msg="Equal")

	def testRegex(self):
		self.assertRegex("this is a test for regex aSSertions", r'[A-Z]', msg="Found")

	def testCountEqual(self):
		self.assertCountEqual([2, 1, 4, 5], (1, 2, 4, 5), msg=True)