from typing import Union
from ..helpers import DataValidators


class DomainValidations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_saving_accounts(country: str, age: Union[int, float]):
        if DataValidators.validate_country(
            country=country, needed_country="COL"
        ) and DataValidators.validate_age(age=age, needed_age=18):
            return True
        return False

    @staticmethod
    def validate_debit_card(
        country: str, age: Union[int, float], incomes: Union[int, float]
    ) -> bool:
        if (
            DataValidators.validate_country(country=country, needed_country="COL")
            and DataValidators.validate_age(age=age, needed_age=18)
            and DataValidators.validate_incomes(incomes=incomes, needed_incomes=1300000)
        ):
            return True
        return False

    @staticmethod
    def validate_credit_card(
        country: str, age: Union[int, float], incomes: Union[int, float]
    ):
        if (
            DataValidators.validate_country(country=country, needed_country="COL")
            and DataValidators.validate_age(age=age, needed_age=20)
            and DataValidators.validate_incomes(incomes=incomes, needed_incomes=2500000)
        ):
            return True
        return False

    @staticmethod
    def validate_insurance(age: Union[int, float], incomes: Union[int, float]):
        if DataValidators.validate_age(
            age=age, needed_age=15
        ) and DataValidators.validate_incomes(incomes=incomes, needed_incomes=800000):
            return True
        return False

    @staticmethod
    def validate_investments(age: Union[int, float], incomes: Union[int, float]):
        if DataValidators.validate_age(
            age=age, needed_age=25
        ) and DataValidators.validate_incomes(incomes=incomes, needed_incomes=4500000):
            return True
        return False

    @staticmethod
    def validate_covered_cards(
        age: Union[int, float], main_card_balance: Union[int, float]
    ) -> Union[int, bool]:
        if DataValidators.validate_age(age=age, needed_age=15):
            return DataValidators.validate_percentage_of_covered_card(
                main_card_balance=main_card_balance, percentage_to_apply=5
            )
        return False
 