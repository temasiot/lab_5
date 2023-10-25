from unittest import TestCase, main
from Task5 import func


class Test(TestCase):
    def test_func(self):
        self.assertEqual(func(5, 2, []), 10)


if __name__ == "__main__":
    main()
