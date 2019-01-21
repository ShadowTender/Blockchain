class Blockchain(object):

    def __init__(self):
        self.chain = [] # contains the blockchain
        self.wallets = dict() # Contains the amount of coin each user owns
        self.wallets["admin"] = 100000000000000

    def add_block(self, block):
        # Add a block to the chain
        # It needs to check if a block is correct
        # Returns True if the block was added, False otherwise
        if block.is_proof_ready() and self.check_legal_transactions(block) :
            self.chain.append(block)
            self.update_wallet(block)
            return True
        else:
            return False

    def update_wallet(self, block):
        # Update the values in the wallet
        # We assume the block is correct
        for trans in block.transactions:
            if trans.receiver not in self.wallets:
                self.wallets[trans.receiver]=0
            self.wallets[trans.receiver] += trans.amount
            self.wallets[trans.sender] -= trans.amount


    def check_legal_transactions(self, block):
        # Check if the transactions of a block are legal given the current state
        # of the chain and the wallet
        # Returns a boolean
        wallets = self.wallets.copy()
        for trans in block.transactions:
            if trans.sender not in wallets:
                return False
            if trans.receiver not in wallets:
                wallets[trans.receiver]=0
            wallets[trans.sender]-=trans.amount
            wallets[trans.receiver]+=trans.amount
            if wallets[trans.sender]<0:
                return False
        return True
