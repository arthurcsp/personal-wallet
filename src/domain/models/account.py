from typing import Optional


class Account:
    def __init__(self, name: str, account_type: str ,  initial_balance :float = 0):
          self.name = name
          self.type = account_type
          self.balance = initial_balance

    def update_balance(self, movemented_amount):
         self.balance = + movemented_amount