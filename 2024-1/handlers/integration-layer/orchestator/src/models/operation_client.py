class OperationClient:
    def __init__(
        self, id, complete_name, password, age, incomes, country, city, operation
    ) -> None:
        self.id = id
        self.complete_name = complete_name
        self.password = password
        self.age = age
        self.incomes = incomes
        self.country = country
        self.city = city
        self.operation = operation

