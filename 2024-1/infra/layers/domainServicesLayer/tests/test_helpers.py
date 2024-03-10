from src.helpers import DataValidators
import pytest


@pytest.mark.helpers
class TestDataValidators:

    @pytest.mark.parametrize(
        "country, needed_country, expected",
        [
            ("COL", "COL", True),
            ("colombia", "COL", True),
            ("colombia", "MEX", False),
            ("lombia", "COL", False),
        ],
    )
    def test_validate_country(self, country, needed_country, expected):
        result = DataValidators.validate_country(country, needed_country)
        assert result == expected

    @pytest.mark.parametrize(
        "age, needed_age, expected",
        [
            (20, 18, True),
            (18, 18, True),
            (17, 18, False),
            (10, 8, True),
        ],
    )
    def test_validate_age(self, age, needed_age, expected):
        result = DataValidators.validate_age(age, needed_age)
        assert result == expected

    @pytest.mark.parametrize(
        "incomes, needed_incomes, expected",
        [
            (10000000, 1300000, True),
            (100000, 1300000, False),
            (10000000, 2500000, True),
            (100000, 2500000, False),
            (10000000, 4500000, True),
            (100000, 4500000, False),
        ],
    )
    def test_validate_incomes(self, incomes, needed_incomes, expected):
        result = DataValidators.validate_incomes(incomes, needed_incomes)
        assert result == expected

    @pytest.mark.parametrize(
        "main_card_balance, percentage, expected",
        [
            (10000000, 5, 500000),
            (1000000, 15, 150000),
            (1000000, 20, 200000),
            (6600000, 5, 330000),
            (14567234, 5, 728361.7),
        ],
    )
    def test_validate_percentage_covered_card(
        self, main_card_balance: int, percentage: int, expected
    ):
        result = DataValidators.validate_percentage_of_covered_card(
            main_card_balance=main_card_balance, percentage_to_apply=percentage
        )
        assert result == expected
