from unittest import TestCase, main
from Task1 import func


class Test(TestCase):
    def test_func(self):
        self.assertEqual(func(4,2,3), 11)


if __name__ == "__main__":
    main()
