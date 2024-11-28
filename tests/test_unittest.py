import unittest

def add_numbers(a, b):
    return a + b

class TestMyModule(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(add_numbers(-1, 1), 0) # -1 + 1 = 0
        self.assertNotEqual(add_numbers(2, 2), 5)  # 2 + 2 ≠ 5

if __name__ == '__main__':
    unittest.main()
