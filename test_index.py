import unittest
from index import sub, sum, mul


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3
        assert sum(0, 0) == 0
        assert sum(-1, 1) == 0
        assert sum(-1, -1) == -2
        assert sum(1, -1) == 0

    def test_sub(self):
        assert sub(1, 2) == -1
        assert sub(0, 0) == 0
        assert sub(-1, 1) == -2
        assert sub(-1, -1) == 0
        assert sub(1, -1) == 2

    def test_mul(self):
        assert mul(1, 2) == 2
        assert mul(0, 0) == 0
        assert mul(-1, 1) == -1
        assert mul(-1, -1) == 1
        assert mul(1, -1) == -1


if __name__ == '__main__':
    unittest.main()
