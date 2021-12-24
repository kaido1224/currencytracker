from django import test

from django.contrib.messages import get_messages

from myapp import forms
from myapp import models
from myapp import tests


class AddEntryViewTest(test.TestCase):
    def setUp(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

    def test_add_get_results(self):
        """Ensure that when adding a new entry, the appropriate context is passed and page loads correctly.
        """
        response = self.client.get("/collection/add")

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(ctx["form"], forms.EntryForm)

    def test_edit_get_results(self):
        """Ensure if editing an existing record, that the appropriate context is returned.
        """
        # Create book record
        book = models.Book.objects.create(
            description="My Test Book"
        )

        # Create currency record.
        entry = models.Currency.objects.create(
            book=book,
            page=1,
            row=3,
            column=2,
            value=5,
            currency="Cent",
            type="Coin",
            country="US"
        )

        response = self.client.get(f"/collection/edit/{entry.id}")

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(ctx["form"], forms.EntryForm)
        self.assertEqual(ctx["entry"], entry)

    def test_invalid_entry_get(self):
        """Ensure that if an invalid entry was entered, that the appropriate message and redirect occurs.
        """
        response = self.client.get("/collection/edit/9999999")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertEqual(messages[0], "Invalid entry specified.")
        self.assertRedirects(response, "/collection", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_post_results(self):
        """Ensure that if a new entry is created, and the user didn't select create another button,
        that the page is redirected back to the collection page.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="My Other Test Book"
        )

        data = {
            "book": book,
            "page": 2,
            "row": 5,
            "column": 4,
            "value": 20,
            "currency": "Euro Cent",
            "country": "FI",
            "type": "Bill"
        }

        response = self.client.post("/collection/add", data=data)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/collection", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Created new entry successfully.")

    def test_post_results_add_another(self):
        """Ensure that if a new entry is created, and the user didn't select create another button,
        that the page is redirected back to the add entry page.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="My Other Test Book"
        )

        data = {
            "book": book,
            "page": 2,
            "row": 5,
            "column": 4,
            "value": 20,
            "currency": "Euro Cent",
            "country": "FI",
            "type": "Bill",
            "_create_another": True
        }

        response = self.client.post("/collection/add", data=data)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/collection/add", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Created new entry successfully.")

    def test_post_results_invalid_form(self):
        """Ensure that if an invalid form occurs, appropriate context is returned.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="Jamie's Test Book"
        )

        data = {
            "book": book,
            "page": 2,
            "row": 5,
            "column": 4,
            "value": 50,
            "currency": "Krone",
            "country": "NO",
            "type": "Test"
        }

        response = self.client.post("/collection/add", data=data)

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(ctx["form"], forms.EntryForm)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertEqual(messages[0], "Form is invalid, make appropriate corrections and try"
                         " again.")

    def test_post_edit_entry_results(self):
        """Ensure that editing an entry the page is redirected back to the collection page if done 
        correctly.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="My Other Test Book"
        )

        # Create currency record.
        entry = models.Currency.objects.create(
            book=book,
            page=1,
            row=3,
            column=2,
            value=5,
            currency="Cent",
            type="Coin",
            country="US"
        )

        data = {
            "book": book,
            "page": 2,
            "row": 5,
            "column": 4,
            "value": 20,
            "currency": "Euro Cent",
            "country": "FI",
            "type": "Bill"
        }

        response = self.client.post(f"/collection/edit/{entry.id}", data=data)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/collection", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Updated entry successfully.")

    def test_post_edit_entry_invalid_form(self):
        """Ensure if an invalid form occurs, that the appropriate context is passed back.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="Austin's Test Book"
        )

        # Create currency record.
        entry = models.Currency.objects.create(
            book=book,
            page=3,
            row=6,
            column=2,
            value=50,
            currency="Krone",
            type="Coin",
            country="NO"
        )

        data = {
            "book": book,
            "page": 2,
            "row": 5,
            "column": 4,
            "value": 50,
            "currency": "Krone",
            "country": "NO",
            "type": "Test"
        }

        response = self.client.post(f"/collection/edit/{entry.id}", data=data)

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ctx["entry"], entry)
        self.assertIsInstance(ctx["form"], forms.EntryForm)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertEqual(messages[0], "Form is invalid, make appropriate corrections and try"
                         " again.")
