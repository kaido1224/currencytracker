from django.contrib.auth.models import User


def setup_test_user():
    """Creates a test user.
    """
    user = User.objects.create(
        username="test",
        password="12345",
        is_active=True
    )

    return user
