"""
Bank account — practises object-oriented programming (classes).

A simple account that can take deposits and withdrawals, refuses to go
overdrawn, and keeps a history of transactions.
Run:  python bank_account.py
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(f"Deposited £{amount:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(f"Withdrew £{amount:.2f}")

    def statement(self) -> None:
        print(f"Account: {self.owner}")
        for line in self.history:
            print(f"  {line}")
        print(f"  Balance: £{self.balance:.2f}")


def main() -> None:
    account = BankAccount("Practice Account", balance=50.0)
    account.deposit(25.0)
    account.withdraw(10.0)
    try:
        account.withdraw(1000.0)      # too much — should be refused
    except ValueError as error:
        print(f"Refused: {error}")
    account.statement()


if __name__ == "__main__":
    main()
