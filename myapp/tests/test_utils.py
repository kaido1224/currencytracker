

from unittest import result
from django import test

from myapp import tests
from myapp import utils


class IsReadOnlyUserTest(test.TestCase):
    def test_read_only_user(self):
        """Test a user whom is in the group Read_Only and ensure this returns True.
        """
        user = tests.setup_test_user(True)

        results = utils.is_read_only_user(user)

        self.assertTrue(results)

    def test_regular_user(self):
        """Test a user not setup in the group Read_Only and ensure this returns False.
        """
        user = tests.setup_test_user()

        results = utils.is_read_only_user(user)

        self.assertFalse(results)


class PopulateCountryListTest(test.TestCase):
    def test_carribean_islands(self):
        """Ensure correct countries are returned when Eastern Carribean Islands is specified as
        a country.
        """
        results = utils.populate_country_list(["CE"])

        expected = ["AI", "AG", "DM", "GD", "MS", "KN", "LC", "VC"]

        self.assertListEqual(results, expected)

    def test_west_africa(self):
        """Ensure correct countries are returned when West Africa CFA is specified as a country.
        """
        results = utils.populate_country_list(["WA"])

        expected = ["BF", "BJ", "CI", "GW", "ML", "NE", "SN", "TG"]

        self.assertListEqual(results, expected)

    def test_central_africa(self):
        """Ensure correct countries are returned when Central Africa CFA is specified as a country.
        """
        results = utils.populate_country_list(["AA"])

        expected = ["CF", "CG", "CM", "GA", "GQ", "TD"]

        self.assertListEqual(results, expected)

    def test_united_states(self):
        """Ensure correct countries are returned when United States of America is specified as a country.
        """
        results = utils.populate_country_list(["US"])

        expected = ["AS", "BQ", "FM", "GU", "MH", "MP", "PR", "TC", "UM", "US", "VG", "VI"]

        self.assertListEqual(results, expected)

    def test_finland(self):
        """Ensure correct countries are returned when Finland is specified as a country.
        """
        results = utils.populate_country_list(["FI"])

        expected = ["AX", "FI"]

        self.assertListEqual(results, expected)

    def test_france(self):
        """Ensure correct countries are returned when France is specified as a country.
        """
        results = utils.populate_country_list(["FR"])

        expected = ["BL", "FR", "MC", "MF", "MQ", "PM", "RE", "TF", "YT"]

        self.assertListEqual(results, expected)

    def test_norway(self):
        """Ensure correct countries are returned when Norway is specified as a country.
        """
        results = utils.populate_country_list(["NO"])

        expected = ["BV", "NO", "SJ"]

        self.assertListEqual(results, expected)

    def test_australia(self):
        """Ensure correct countries are returned when Australia is specified as a country.
        """
        results = utils.populate_country_list(["AU"])

        expected = ["AU", "CC", "CX", "HM", "NF", "NR", "TV"]

        self.assertListEqual(results, expected)

    def test_denmark(self):
        """Ensure correct countries are returned when Denmark is specified as a country.
        """
        results = utils.populate_country_list(["DK"])

        expected = ["DK", "FO", "GL"]

        self.assertListEqual(results, expected)

    def test_united_kingdom(self):
        """Ensure correct countries are returned when United Kingdom is specified as a country.
        """
        results = utils.populate_country_list(["GB"])

        expected = ["GB", "GS", "IO"]

        self.assertListEqual(results, expected)

    def test_new_zealand(self):
        """Ensure correct countries are returned when New Zealand is specified as a country.
        """
        results = utils.populate_country_list(["NZ"])

        expected = ["NU", "NZ", "PN", "TK"]

        self.assertListEqual(results, expected)

    def test_israel(self):
        """Ensure correct countries are returned when Israel is specified as a country.
        """
        results = utils.populate_country_list(["IL"])

        expected = ["IL", "PS"]

        self.assertListEqual(results, expected)
