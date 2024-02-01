from datetime import datetime, date
from registers import Account, Category

class Movements:
    def __init__(self, id, account:Account, category:Category , amount : float , description : str , due_date: date):
        self.id = id
        self.account = account.id
        self.category = category.id
        self.amount = amount
        self.description = description
        self.due_date = due_date
        self.time = datetime.utcnow()
