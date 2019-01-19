class Transaction(object):

    def __init__(self, index, sender, receiver, amount):
        # Store internally
        self.index = index
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.dict={}

    def to_dict(self):
        # Transform object into a dictionary for future transformation in JSON
        # The gave of the fields are the name of the variables
        self.dict['index']=self.index
        self.dict['sender'] = self.sender
        self.dict['receiver'] = self.receiver
        self.dict['amount'] = self.amount
