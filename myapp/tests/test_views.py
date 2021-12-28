from django import test

from django.contrib.messages import get_messages

from myapp import forms
from myapp import models
from myapp import tests


class AddBookViewTest(test.TestCase):
    def setUp(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

    def test_add_get_results(self):
        """Ensure that when adding a new entry, the appropriate context is passed and page loads correctly.
        """
        response = self.client.get("/books/add")

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(ctx["form"], forms.BookForm)

    def test_edit_get_results(self):
        """Ensure if editing an existing record, that the appropriate context is returned.
        """
        # Create book record
        book = models.Book.objects.create(
            description="My Test Book",
            pages=6,
            rows_per_page=5,
            columns_per_row=5
        )

        response = self.client.get(f"/books/edit/{book.id}")

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(ctx["form"], forms.BookForm)
        self.assertEqual(ctx["book"], book)

    def test_invalid_entry_get(self):
        """Ensure that if an invalid entry was entered, that the appropriate message and redirect occurs.
        """
        response = self.client.get("/books/edit/9999999")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertEqual(messages[0], "Invalid book specified.")
        self.assertRedirects(response, "/books", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_post_results(self):
        """Ensure that if a new book is created, and the user didn't select create another button,
        that the page is redirected back to the books page.
        """
        data = {
            "description": "My New Test Book"
        }

        response = self.client.post("/books/add", data=data)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/books", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Created new book successfully.")

    def test_post_results_add_another(self):
        """Ensure that if a new book is created, and the user didn't select create another button,
        that the page is redirected back to the add book page.
        """
        data = {
            "description": "Another Test Book",
            "pages": 2,
            "rows_per_page": 5,
            "columns_per_row": 4,
            "_create_another": True
        }

        response = self.client.post("/books/add", data=data)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/books/add", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Created new book successfully.")

    def test_post_results_invalid_form(self):
        """Ensure that if an invalid form occurs, appropriate context is returned.
        """
        data = {
            "pages": 1
        }

        response = self.client.post("/books/add", data=data)

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(ctx["form"], forms.BookForm)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertEqual(messages[0], "Form is invalid, make appropriate corrections and try"
                         " again.")

    def test_post_edit_book_results(self):
        """Ensure that editing a book the page is redirected back to the books page if done
        correctly.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="My Third Test Book"
        )

        data = {
            "description": "My Third Test Book",
            "pages": 5
        }

        response = self.client.post(f"/books/edit/{book.id}", data=data)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/books", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Updated book successfully.")

    def test_post_edit_book_invalid_form(self):
        """Ensure if an invalid form occurs, that the appropriate context is passed back.
        """
        # Create book record.
        book = models.Book.objects.create(
            description="Shammy's Test Book"
        )

        data = {
            "pages": 5
        }

        response = self.client.post(f"/books/edit/{book.id}", data=data)

        ctx = response.context

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ctx["book"], book)
        self.assertIsInstance(ctx["form"], forms.BookForm)

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertEqual(messages[0], "Form is invalid, make appropriate corrections and try"
                         " again.")


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


class BookViewTest(test.TestCase):
    def setUp(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

    def test_results(self):
        # Create book record.
        book = models.Book.objects.create(
            description="My Book Test"
        )

        response = self.client.get("/books")

        ctx = response.context

        # Get last record
        index = len(ctx["books"]) - 1

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ctx["books"][index], book)
        self.assertFalse(ctx["read_only_user"])


class CollectionViewTest(test.TestCase):
    def setUp(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

    def test_results(self):
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

        response = self.client.get("/collection")

        ctx = response.context

        expected = {
            "book": book,
            "column": 2,
            "country": "United States",
            "currency": "Cent",
            "id": entry.id,
            "page": 1,
            "row": 3,
            "type": "Coin",
            "value": 5
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ctx["results"][-1], expected)
        self.assertFalse(ctx["read_only_user"])

    def test_country_czechoslovakia(self):
        """Ensure that if CS is the country that Czechoslovakia is the country returned.
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
            currency="Koruna",
            type="Coin",
            country="CS"
        )

        response = self.client.get("/collection")

        ctx = response.context

        expected = {
            "book": book,
            "column": 2,
            "country": "Czechoslovakia",
            "currency": "Koruna",
            "id": entry.id,
            "page": 1,
            "row": 3,
            "type": "Coin",
            "value": 5
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ctx["results"][-1], expected)

    def test_country_west_africa(self):
        """Ensure that if WA is the country that West Africa CFA is the country returned.
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
            currency="Franc",
            type="Coin",
            country="WA"
        )

        response = self.client.get("/collection")

        ctx = response.context

        expected = {
            "book": book,
            "column": 2,
            "country": "West Africa CFA",
            "currency": "Franc",
            "id": entry.id,
            "page": 1,
            "row": 3,
            "type": "Coin",
            "value": 5
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ctx["results"][-1], expected)

    def test_country_central_africa(self):
        """Ensure that if WA is the country that Central Africa CFA is the country returned.
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
            currency="Franc",
            type="Coin",
            country="AA"
        )

        response = self.client.get("/collection")

        ctx = response.context

        expected = {
            "book": book,
            "column": 2,
            "country": "Central Africa CFA",
            "currency": "Franc",
            "id": entry.id,
            "page": 1,
            "row": 3,
            "type": "Coin",
            "value": 5
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ctx["results"][-1], expected)

    def test_country_eastern_carribean(self):
        """Ensure that if CE is the country that Eastern Carribean is the country returned.
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
            country="CE"
        )

        response = self.client.get("/collection")

        ctx = response.context

        expected = {
            "book": book,
            "column": 2,
            "country": "Eastern Carribean Islands",
            "currency": "Cent",
            "id": entry.id,
            "page": 1,
            "row": 3,
            "type": "Coin",
            "value": 5
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(ctx["results"][-1], expected)


class DeleteBookViewTest(test.TestCase):
    def setUp(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

        # Create book record.
        self.book = models.Book.objects.create(
            description="My Deletion Test Book"
        )

    def test_results(self):
        response = self.client.post(f"/books/delete/{self.book.id}")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/books", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Successfully deleted book and all it's entries.")

    def test_invalid_book(self):
        invalid_entry = models.Book.objects.count() + 1

        response = self.client.post(f"/books/delete/{invalid_entry}")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/books", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Failed to delete book.")


class DeleteEntryViewTest(test.TestCase):
    def setUp(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

        # Create book record.
        book = models.Book.objects.create(
            description="My Other Test Book"
        )

        # Create currency record.
        self.entry = models.Currency.objects.create(
            book=book,
            page=1,
            row=3,
            column=2,
            value=5,
            currency="Cent",
            type="Coin",
            country="US"
        )

    def test_results(self):
        response = self.client.post(f"/collection/delete/{self.entry.id}")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/collection", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Successfully deleted entry.")

    def test_invalid_entry(self):
        invalid_entry = models.Currency.objects.count() + 1

        response = self.client.post(f"/collection/delete/{invalid_entry}")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/collection", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "Failed to delete entry.")


class IndexViewTest(test.TestCase):
    def test_results(self):
        user = tests.setup_test_user()
        self.client.force_login(user=user)

        # Create book record.
        book = models.Book.objects.create(
            description="My Other Test Book"
        )

        # Create currency record.
        models.Currency.objects.create(
            book=book,
            page=1,
            row=3,
            column=2,
            value=5,
            currency="Franc",
            type="Coin",
            country="WA"
        )

        response = self.client.get("/")

        ctx = response.context

        # Ensure these context values are present.
        self.assertIsNotNone(ctx["countries"])
        self.assertIsNotNone(ctx["missing_countries"])
