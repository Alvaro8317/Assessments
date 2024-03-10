from typing import Union


class DataValidators:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_country(country: str, needed_country: str) -> bool:
        return True if country.upper().startswith(needed_country) else False

    @staticmethod
    def validate_age(age: Union[int, float], needed_age: int) -> bool:
        return True if age >= needed_age else False

    @staticmethod
    def validate_incomes(
        incomes: Union[int, float], needed_incomes: Union[int, float]
    ) -> bool:
        return True if incomes > needed_incomes else False

    @staticmethod
    def validate_percentage_of_covered_card(
        main_card_balance: Union[int, float], percentage_to_apply: Union[int, float]
    ) -> bool:
        return (main_card_balance * percentage_to_apply) / 100
