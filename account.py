

class Account:
    def __init__(self, name: str) -> None:
        """
        Assigns an Account Name and Account Balance to an Account object when it is instantiated.
        :param name: Account name.
        """
        self.__account_name = name
        self.__account_balance: float = 0
    
    def deposit(self, amount: float) -> bool:
        """
        Method to add money to an account.
        :param amount: The deposit amount.
        :return: True if deposit is succesful, otherwise False.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Method to deduct money from an account.
        :param amount: The withdrawal amount.
        :return: True if withdrawal is succesful, otherwise False.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True
    
    def get_balance(self) -> float:
        """
        Method to access an account's balance.
        :return: The account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to modify an account's balance.
        :return: The account name.
        """
        return self.__account_name


