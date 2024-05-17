"""Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato."""

class Account:
    
    def __init__(self, account_id: str, balance: float):
        self.account_id : str = account_id
        self.balance : float = balance


    def deposit(self, amount: float):
        self.amount : float = amount
        self.balance += amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance

class Bank:

    def __init__(self, accounts: dict[str, Account]={}):
        accounts : Account = {}
        self.accounts: dict[str, Account] = accounts

    
    def create_account(self, account_id: str, balance: float =0):
        self.account_id: str = account_id
        self.balance: float = balance
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id, balance)
            return self.accounts[account_id]
        else:
            raise ValueError("Account with this ID already exists.")

    def deposit(self, account_id: str, amount: float):
        if account_id in self.accounts.keys():
            self.accounts[account_id].deposit(amount)
        else :
            raise ValueError("Account not found")

    def get_balance(self, account_id : str):
        if account_id in self.accounts.keys():
            return self.accounts[account_id].get_balance()
        else :
            raise ValueError("Account not found")
    

"""bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)"""


bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))