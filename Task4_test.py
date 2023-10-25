from unittest import TestCase, main
from Task4 import S0, S1, S2,S3, S4


class Test(TestCase):
    def test_S0(self):
        self.assertEqual(S0(1,5), 2.1153846153846154)
    def test_S1(self):
        self.assertEqual(S1(1,5, 1), 2.1153846153846154)
    def test_S2(self):
        self.assertEqual(S2(1,5, 5), 2.1153846153846154)
    def test_S3(self):
        self.assertEqual(S3(1,5, 1, 0), 2.1153846153846154)
    def test_S4(self):
        self.assertEqual(S4(1,5, 5, 0), 2.1153846153846154)


if __name__ == "__main__":
    main()
