import json

from block_header import BlockHeader
from transaction import Transaction
from block import Block
from blockchain import Blockchain


def read_header(header):
    # Implement these functions to help you
    # Takes a dictionary as an input
    return BlockHeader(header['index'],header['nonce'],header['previous_hash'],header['timestamp'])
    
def read_transaction(transaction):
    # Same above for transformation
    return Transaction(transaction['index'],transaction['sender'],transaction['receiver'],transaction['amount'])

def read_block(block):
    # Reads a block from a dictionary
    return Block(read_header(block['header']),[read_transaction(item) for item in block['transactions']])

def read_block_json(block_json):
    # Reads a block in json format
    return read_block(json.loads(block_json))

def read_chain(chain):
    # read the chain from a json str
    # Returns a list of Block
    # This method does not do any checking
    return [read_block(item )for item in json.loads(chain)]





