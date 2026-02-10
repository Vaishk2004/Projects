class Blood :
    def __init__(self,bid=0,bgroup="",count=0,expDate=0):
        self.bid = bid
        self.bgroup = bgroup
        self.count = count
        self.expDate = expDate

    def __str__(self):
        return f"{self.bid},{self.bgroup},{self.count},{self.expDate}\n"
    
    