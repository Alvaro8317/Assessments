from typing import Union
from ..helpers import DataValidators


class DomainValidations:
    validation_result_of_saving_accounts: bool = False
    validation_result_of_saving_accounts: bool = False
    validation_result_of_debit_card: bool = False
    validation_result_of_credit_card: bool = False
    validation_result_of_insurance: bool = False
    validation_result_of_investments: bool = False
    validation_result_of_covered_cards: Union[int, float] = 0

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

    @classmethod
    def validate_all_products(cls, user_data: dict) -> dict:
        country_user = user_data["country"]
        age_user = user_data["age"]
        incomes_user = user_data["incomes"]
        cls.validation_result_of_saving_accounts = (
            DomainValidations.validate_saving_accounts(
                country=country_user, age=age_user
            )
        )
        cls.validation_result_of_debit_card = DomainValidations.validate_debit_card(
            country=country_user, age=age_user, incomes=incomes_user
        )
        cls.validation_result_of_credit_card = DomainValidations.validate_credit_card(
            country=country_user, age=age_user, incomes=incomes_user
        )
        cls.validation_result_of_insurance = DomainValidations.validate_insurance(
            age=age_user, incomes=incomes_user
        )
        cls.validation_result_of_investments = DomainValidations.validate_investments(
            age=age_user, incomes=incomes_user
        )
        cls.validation_result_of_covered_cards = (
            DomainValidations.validate_covered_cards(
                age=age_user, main_card_balance=incomes_user
            )
        )
        return {
            "validation_result_of_saving_accounts": cls.validation_result_of_saving_accounts,
            "validation_result_of_saving_accounts": cls.validation_result_of_saving_accounts,
            "validation_result_of_debit_card": cls.validation_result_of_debit_card,
            "validation_result_of_credit_card": cls.validation_result_of_credit_card,
            "validation_result_of_insurance": cls.validation_result_of_insurance,
            "validation_result_of_investments": cls.validation_result_of_investments,
            "validation_result_of_covered_cards": cls.validation_result_of_covered_cards,
        }
