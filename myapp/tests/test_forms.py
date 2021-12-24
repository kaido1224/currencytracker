import datetime

from django import test

from myapp import forms
from myapp import tests
from myapp.models import Book


class EntryFormTest(test.TestCase):
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

    def test_country_not_specified(self):
        """If country not specified, ensure it is still valid.
        """
        data = {
            "country": ""
        }

        form = self.form_data(**data)

        self.assertTrue(form.is_valid())

    def test_invalid_type(self):
        """Ensure that if an invalid type is specified an error occurs.
        """
        data = {
            "type": "Test"
        }

        form = self.form_data(**data)

        errors = form.errors.as_data()

        self.assertFalse(form.is_valid())
        self.assertEqual(len(errors), 1)
        self.assertEqual(form["type"].errors.as_data()[0].code, "invalid_choice")

    def test_valid_form(self):
        """Test what is expected to be valid results.
        """
        form = self.form_data()

        self.assertTrue(form.is_valid())
