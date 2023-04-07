from dataclasses import dataclass

@dataclass()
class BankOperation:
    bank_account:str
    amount:float
    date_time:str