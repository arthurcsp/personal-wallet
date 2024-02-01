class Account:
     def __init__(self, id:int, name: str, account_type: str ,  initial_balance :float = 0):
          self.id = id
          self.name = name
          self.type = account_type
          self.balance = initial_balance


class Category:
     def __init__(self, id:int, name:str, subcategory:str, group:str):
          self.id = id
          self.name = name
          self.subcategory = subcategory
          self.group = group