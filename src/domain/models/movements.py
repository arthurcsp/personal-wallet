from datetime import datetime

class Movements:
    def __init__(self, account :str, category : str , time: datetime , amount : float ):
        self.account = account
        self.category = category
        self.time = time
        self.amount = amount
