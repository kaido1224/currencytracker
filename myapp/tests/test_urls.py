from django import test

from django.urls import reverse


# Test page link functionality.
class PageLinksTest(test.TestCase):
    def test_home_page(self):
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse("myapp:index"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_books_page(self):
        response = self.client.get("/books", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_books_page_by_name(self):
        response = self.client.get(reverse("myapp:books"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_book_page(self):
        response = self.client.get("/books/add", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_book_page_by_name(self):
        response = self.client.get(reverse("myapp:add_book"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_book_page(self):
        response = self.client.get("/books/edit/1", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book_page(self):
        response = self.client.get("/books/delete/1", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_collection_page(self):
        response = self.client.get("/collection", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_collection_page_by_name(self):
        response = self.client.get(reverse("myapp:collection"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_entry_page(self):
        response = self.client.get("/collection/add", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_entry_page_by_name(self):
        response = self.client.get(reverse("myapp:add_entry"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_entry_page(self):
        response = self.client.get("/collection/edit/1", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_entry_page(self):
        response = self.client.get("/collection/delete/1", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page_by_name(self):
        response = self.client.get(reverse("myapp:login"), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get("/logout", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_page_by_name(self):
        response = self.client.get(reverse("myapp:logout"), follow=True)
        self.assertEqual(response.status_code, 200)
