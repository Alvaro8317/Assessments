from typing import Union
import pytest
from src import DomainValidations


@pytest.mark.domain
class TestDomainValidations:

    @pytest.mark.parametrize(
        "country, age, expected",
        [
            ("COL", 18, True),
            ("colombia", 26, True),
            ("perú", 19, False),
            ("COLOMBIA", 17, False),
        ],
    )
    def test_validate_saving_accounts(
        self, country: str, age: Union[int, float], expected: bool
    ):
        result = DomainValidations.validate_saving_accounts(country, age)
        assert result == expected

    @pytest.mark.parametrize(
        "country, age, incomes, expected",
        [
            ("COLOMBIA", 20, 1500000, True),
            ("PERÚ", 20, "1500000", False),
            ("COLOMBIA", 20, 150000, False),
            ("COLOMBIA", 15, 1500000, False),
        ],
    )
    def test_validate_debit_card(
        self,
        country: str,
        age: Union[int, float],
        incomes: Union[int, float],
        expected: bool,
    ):
        result = DomainValidations.validate_debit_card(country, age, incomes)
        assert result == expected

    @pytest.mark.parametrize(
        "country, age, incomes, expected",
        [
            ("Colombia", 26, 6600000, True),
            ("Perú", 26, 6600000, False),
            ("Colombia", 19, 6600000, False),
            ("Colombia", 26, 2000000, False),
        ],
    )
    def test_validate_credit_card(
        self,
        country: str,
        age: Union[int, float],
        incomes: Union[int, float],
        expected: bool,
    ):
        result = DomainValidations.validate_credit_card(country, age, incomes)
        assert result == expected

    @pytest.mark.parametrize(
        "age, incomes, expected",
        [
            (16, 1000000, True),
            (18, 900000, True),
            (14, 1000000, False),
            (16, 100000, False),
        ],
    )
    def test_validate_insurance(
        self, age: Union[int, float], incomes: Union[int, float], expected: bool
    ):
        result = DomainValidations.validate_insurance(age=age, incomes=incomes)
        assert result == expected

    @pytest.mark.parametrize(
        "age, incomes, expected",
        [
            (28, 10000000, True),
            (18, 10000000, False),
            (34, 4000000, False),
            (66, 100000, False),
        ],
    )
    def test_validate_investments(
        self, age: Union[int, float], incomes: Union[int, float], expected: bool
    ):
        result = DomainValidations.validate_investments(age=age, incomes=incomes)
        assert result == expected

    @pytest.mark.parametrize(
        "age, main_card_balance, expected",
        [
            (16, 14567234, 728361.7),
            (14, 14567234, False),
            (20, 1000000, 50000),
        ],
    )
    def test_covered_cards(
        self,
        age: Union[int, float],
        main_card_balance: Union[int, float],
        expected: Union[bool, int, float],
    ):
        result = DomainValidations.validate_covered_cards(
            age=age, main_card_balance=main_card_balance
        )
        assert result == expected
