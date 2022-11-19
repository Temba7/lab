class Account:

    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

        '''
        Function contain name and set account balance to 0
        '''



    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    '''
    Function increment the account balance by decimal number greater than 0
    '''

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.__account_balance:
            return False

        else:
            self.__account_balance -= amount
            return True

    '''
    Function decrement the account balance by decimal number greater than 0
    '''

    def get_balance(self) -> float:
        return self.__account_balance

    '''
    Function return the account balance
    '''

    def get_name(self) -> str:
        return self.__account_name

    '''
       Function return the initial name
       '''


















