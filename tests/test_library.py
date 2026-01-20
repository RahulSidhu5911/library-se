import unittest
from src.library import Library


class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("101", "Python", "Guido")
        self.assertIn("101", self.library.books)

    def test_duplicate_book(self):
        self.library.add_book("101", "Python", "Guido")
        with self.assertRaises(ValueError):
            self.library.add_book("101", "Java", "James")


class TestLibrarySprint2(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("101", "Python", "Guido")

    def test_borrow_book(self):
        self.library.borrow_book("101")
        self.assertEqual(self.library.books["101"]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        self.library.borrow_book("101")
        with self.assertRaises(ValueError):
            self.library.borrow_book("101")

    def test_return_book(self):
        self.library.borrow_book("101")
        self.library.return_book("101")
        self.assertEqual(self.library.books["101"]["status"], "Available")


class TestLibrarySprint3(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("101", "Python", "Guido")

    def test_report_header(self):
        report = self.library.generate_report()
        self.assertIn("BookID", report[0])

    def test_report_has_book(self):
        report = self.library.generate_report()
        self.assertTrue(len(report) > 1)


if __name__ == "__main__":
    unittest.main()
