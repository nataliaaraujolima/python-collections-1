from dataclasses import dataclass


@dataclass
class SteamAccount:
    user: str
    balance: float = 0.0

    @staticmethod
    def add_balance(account, value: float) -> None:
        account.balance += value

    @staticmethod
    def view_balance(account) -> None:
        print(account.balance)

    def buy_game(account, price: float) -> None:
        if account.balance >= price:
            account.balance -= price
        else:
            print("Nao tem money")

    def view_user(account) -> None:
        print(account.user)


# Criando uma instância de SteamAccount
populating_attributes = SteamAccount('Alucard', 100.40)
# print(populating_attributes)

add = SteamAccount.add_balance(populating_attributes, 200.3)
print(add)
