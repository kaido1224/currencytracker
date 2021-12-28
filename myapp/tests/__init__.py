from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def setup_test_user(read_only=False):
    """Creates a test user.

    Arguments:
        read_only_user: Optional boolean used to determine whether user should be setup as a
        read_only user or not. Default is False.
    """
    ro = Group.objects.get(name="Read_Only")

    user = User.objects.create(
        username="test",
        password="12345",
        is_active=True
    )
    if read_only:
        user.groups.add(ro)

    user.save()

    return user
