import json
import hashlib

class Block(object):

    def __init__(self, header, transactions):
        # Store everything internally
        # header is a BlockHeader and transaction is a list of Transaction
        self.header = header
        self.transactions = transactions
        self.N_STARTING_ZEROS = 4

    def to_dict(self):
        # Turns the object into a dictionary
        # There are two fields: header and transactions
        # The values are obtained by using the to_dict methods
        dict={}
        dict['header'] = self.header
        dict['transactions'] = self.transactions
        return dict

    def to_json(self):
        # Transforms into a json string
        # use the option sort_key=True to make the representation unique
        return json.dumps(self.to_dict(),sort_key=True)
    

    def is_proof_ready(self):
        # Check whether the block is proven
        # For that, make sure the hash begins by N_STARTING_ZEROS
        hstring = self.header.get_hash()
        return hstring.startswith('0'*self.N_STARTING_ZEROS,0)
       

    def make_proof_ready(self):
        # Transforms the block into a proven block
        number = 0
        if self.is_proof_ready():
            print('nonce:',self.header.nonce,'hash:',self.header.get_hash())
        else:
            while not self.is_proof_ready():
                self.header.set_nonce(number)
                number+=1
            print('nonce: {}, hash:{}'.format(self.header.nonce,self.header.get_hash()))

    def set_zeros(self,number):
        self.N_STARTING_ZEROS=number
