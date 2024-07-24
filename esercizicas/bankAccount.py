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

class Account():

    def __init__(self,account_id: str, balance: float):
        self.account_id : str = account_id
        self.balance : float = balance

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance
    
    def get_balance(self)->float:
        return self.balance
    
class Bank():

    def __init__(self) -> None:
        self.accounts : dict[str,Account] = {}

    def create_account(self, account_id: str):
        if account_id in self.accounts:
            return "Account with this ID already exist"
        else:
            new_account : Account = Account(account_id, balance=0)
            self.accounts[account_id] = new_account
            return self.accounts
    
    def deposit(self, account_id: str, amount: float):
        for k,v in self.accounts.items():
            if account_id in k:
                v.deposit(amount)
            else:
                return
        return self.accounts
    
    def get_balance(self,account_id: str):
        for k,v in self.accounts.items():
            if account_id in k:
                return v.get_balance()
        print("Account not found")
            
        
