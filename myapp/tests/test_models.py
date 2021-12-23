from django import test
from django.db import IntegrityError
from django.utils import timezone

from myapp import models


class BookTest(test.TestCase):
    def create_book(self):
        """Create a book instance.
        """
        book = models.Book.objects.create(
            description="Test Book",
            pages=7
        )

        return book

    def test_create(self):
        """Test successful creation of a book.
        """
        book = self.create_book()

        gmt = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        created_ts = book.created_ts.strftime("%Y-%m-%d %H:%M:%S")
        updated_ts = book.updated_ts.strftime("%Y-%m-%d %H:%M:%S")

        self.assertEqual(book.description, "Test Book")
        self.assertEqual(book.pages, 7)
        self.assertEqual(updated_ts, gmt)
        self.assertEqual(created_ts, gmt)

    def test_update_record(self):
        """Ensure that when record is updated, the updated_ts changes but the created_ts does not.
        """
        book = self.create_book()

        created_ts = book.created_ts
        updated_ts = book.updated_ts

        b = models.Book.objects.get(pk=book.id)
        b.description = "Test Book 2"
        b.save()

        self.assertEqual(created_ts, b.created_ts)
        self.assertNotEqual(updated_ts, b.updated_ts)

    def test_delete_record(self):
        """Ensure that record and associated currency are removed when deleted.
        """
        book = self.create_book()

        # Create a collection record associated to the book.
        c = models.Currency.objects.create(book=book, country="US")

        models.Book.objects.get(pk=book.id).delete()

        with self.assertRaises(models.Book.DoesNotExist):
            models.Book.objects.get(pk=book.id)

        with self.assertRaises(models.Currency.DoesNotExist):
            models.Currency.objects.get(pk=c.id)


class CurrencyTest(test.TestCase):
    def create_entry(self):
        """Create a currency instance.
        """
        # Create a book to associate to the currency record.
        self.book = models.Book.objects.create(
            description="Test Book",
            pages=7
        )

        entry = models.Currency.objects.create(
            book=self.book,
            page=1,
            row=1,
            column=1,
            currency="Penny",
            value=1,
            type="Coin",
            country="GB"
        )

        return entry

    def test_create_record_no_book(self):
        """If a book is not attached to the record, ensure error is thrown.
        """
        with self.assertRaises(IntegrityError):
            models.Currency.objects.create(
                page=1,
                row=1,
                column=1,
                currency="Penny",
                value=1,
                type="Coin",
                country="GB"
            )

    def test_create_record(self):
        """Test successful creation of a currency entry.
        """
        entry = self.create_entry()

        gmt = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        created_ts = entry.created_ts.strftime("%Y-%m-%d %H:%M:%S")
        updated_ts = entry.updated_ts.strftime("%Y-%m-%d %H:%M:%S")

        self.assertEqual(entry.book, self.book)
        self.assertEqual(entry.page, 1)
        self.assertEqual(entry.row, 1)
        self.assertEqual(entry.column, 1)
        self.assertEqual(entry.currency, "Penny")
        self.assertEqual(entry.value, 1)
        self.assertEqual(entry.type, "Coin")
        self.assertEqual(entry.country, "GB")
        self.assertEqual(updated_ts, gmt)
        self.assertEqual(created_ts, gmt)

    def test_update_record(self):
        """Ensure that when record is updated, the updated_ts changes but the created_ts does not.
        """
        entry = self.create_entry()

        created_ts = entry.created_ts
        updated_ts = entry.updated_ts

        c = models.Currency.objects.get(pk=entry.id)
        c.country = "US"
        c.save()

        self.assertEqual(created_ts, c.created_ts)
        self.assertNotEqual(updated_ts, c.updated_ts)

    def test_delete_record(self):
        """Ensure that record is removed when deleted.
        """
        entry = self.create_entry()

        models.Currency.objects.get(pk=entry.id).delete()

        with self.assertRaises(models.Currency.DoesNotExist):
            models.Currency.objects.get(pk=entry.id)
