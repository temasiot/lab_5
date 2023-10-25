from unittest import TestCase, main
from Task3 import s


class Test(TestCase):
    def test_s(self):
        self.assertEqual(s(0), 2)


if __name__ == "__main__":
    main()
