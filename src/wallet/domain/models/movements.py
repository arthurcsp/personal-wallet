from datetime import datetime
from domain.models.registers import Account, Category

class Movements:
    def __init__(self, account:Account, category:Category , amount : float , description : str , id:int = None):
        self.id = id
        self.account = account.id
        self.category = category.id
        self.amount = amount
        self.description = description
        self.time = datetime.utcnow()
