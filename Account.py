class Account:
    """
    A class used to represent a bank account.

    The class will track the current balance of the account and will not allow the user to withdraw more money
    than is currently in the account. The user also has the ability to deposit more money into the account.

    Attributes:
        __balance: int (private)
            the current balance of the account

    Methods:
        withdraw(int, boolean=True) -> None or int
            Attempts to withdraw money from the account. If there are insufficient funds, returns None. Otherwise
            returns the amount to withdraw

        deposit(int) -> None
            Deposits money into the account. Returns None.

        get_balance() -> int
            Returns the current balance.
    """
    def __init__(self, balance=0):
        """
        Parameters
        ----------
            balance: int, optional
                The starting balance of the account. (Default 0).
        """
        pass

    def withdraw(self, amount_to_withdraw, quiet=True):
        """
        Attempt to withdraw money from the account. Return None if there are insufficient funds, otherwise returns
        the amount that was withdrawn. Optionally, an error message will be printed if `quiet` is False

        Parameters
        ----------
            amount_to_withdraw: int
                The amount to attempt to withdraw
            quiet: boolean, optional
                If set to False, an error message is printed if there are insufficient funds to withdraw. (Default is
                True)
        """
        pass

    def deposit(self, amount_to_deposit):
        """
        Adds money to the account. Returns nothing.

        Parameters
        ----------
            amount_to_deposit: int
                The amount to add to the account
        """
        pass

    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        pass

