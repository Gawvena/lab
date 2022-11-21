class Account(name=input()):

    def __init__(self, name: str):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        """
        This function is used to add the amount specified to the account balance

        :param amount: This is the amount to be added
        :return: Whether the process was successful or not
        """
        if amount >= 0 or amount <= self.__account_balance:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float):
        """
        This function is used to subtract the amount specified from the account balance

        :param amount: This is the amount to be subtracted
        :return: Whether the process was successful or not
        """

        if amount >= 0:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Returns the account's balance
        :return: The account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Returns the account's name
        :return: The account name
        """
        return self.__account_name
