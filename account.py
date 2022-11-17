

class Account:
<<<<<<< Updated upstream
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount: float) -> bool:
=======
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount):
>>>>>>> Stashed changes
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    
<<<<<<< Updated upstream
    def withdraw(self, amount: float) -> bool:
=======
    def withdraw(self, amount):
>>>>>>> Stashed changes
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True
<<<<<<< Updated upstream
=======
    
    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
>>>>>>> Stashed changes


