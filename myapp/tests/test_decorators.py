from django import test

from django.contrib.messages import get_messages

from myapp import tests


class IsReadOnlyUserTest(test.TestCase):
    def test_read_only_user(self):
        """Test a user whom is in the group Read_Only and when they try to go to a page with this
        method decorator, ensure they are redirected appropriately.
        """
        user = tests.setup_test_user(True)
        self.client.force_login(user=user)

        response = self.client.get("/books/add")

        messages = [m.message for m in get_messages(response.wsgi_request)]

        self.assertRedirects(response, "/", status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(messages[0], "You don't have permission to view this page.")

    def test_regular_user(self):
        """Test a user whom is not associated to the Read_Only group, ensure when trying to 
        go to a page with this method decorator, that they are able to do so.
        """
        user = tests.setup_test_user(False)
        self.client.force_login(user=user)

        response = self.client.get("/books/add")

        self.assertEqual(response.status_code, 200)

    def test_anonymous_user(self):
        """Test an anonymous user, ensure that they are redirected to the login page.
        """
        response = self.client.get("/books/add")

        self.assertRedirects(response, "/login/?next=/", status_code=302, target_status_code=200,
                             fetch_redirect_response=True)
