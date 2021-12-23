import datetime

from django import test

from myapp import forms
from myapp.models import Book


class EntryFormTest(test.TestCase):
    def setUp(self):
        self.now = datetime.datetime.now()

    def form_data(self, **kwargs):
        data = {}

        book = Book.objects.create(description="Test Book")

        data["book"] = kwargs.pop("book", book)
        data["page"] = kwargs.pop("page", 1)
        data["row"] = kwargs.pop("row", 1)
        data["column"] = kwargs.pop("column", 1)
        data["currency"] = kwargs.pop("currency", "Cent")
        data["value"] = kwargs.pop("value", "1")
        data["type"] = kwargs.pop("type", "Coin")
        data["country"] = kwargs.pop("country", "US")

        return forms.EntryForm(
            data=data
        )

    def test_no_book_specified(self):
        """If book not specified, ensure error is thrown.
        """
        data = {
            "book": ""
        }

        form = self.form_data(**data)

        errors = form.errors.as_data()

        self.assertFalse(form.is_valid())
        self.assertEqual(len(errors), 1)
        self.assertEqual(form["book"].errors.as_data()[0].code, "required")
