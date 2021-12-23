from typing import Collection
from django import test

from myapp import models
from myapp import utils


class PopulateCountryListTest(test.TestCase):
    def test_carribean_islands(self):
        """Ensure the correct countries are returned when Eastern Carribean Islands is specified as
        the country.
        """

        # Create book
        book = models.Book.objects.create(description="Test 1")

        # Create test collection value
        models.Currency.objects.create(book=book, value="1", country="CE")

        results = utils.populate_country_list(["CE"])

        expected = ["AI", "AG", "DM", "GD", "MS", "KN", "LC", "VC"]

        self.assertListEqual(results, expected)
