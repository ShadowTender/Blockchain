import json
import hashlib


class BlockHeader(object):

    def __init__(self, index, nonce, previous_hash, timestamp):
        # Store internally
        self.index = index 
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = nonce

    def to_dict(self):
        # Transform object into a dictionary for future transformation in JSON
        # The gave of the fields are the name of the variables
        dict={}
        dict['index'] = self.index
        dict['previous_hash'] = self.previous_hash
        dict['nonce'] = self.nonce
        dict['timestamp'] = self.timestamp
        return dict

    def to_json(self):
        # Transforms into a json string
        # use the option sort_key=True to make the representation unique
        return json.dumps(self.to_dict(),sort_keys=True)

    def set_nonce(self, new_nonce):
        # Set the nonce value
        self.nonce = new_nonce 
        pass

    def get_hash(self):
        # Use hashlib to hash the block using sha256
        # Use hexdigest to get a string result
        return hashlib.sha256(self.to_json().encode('utf-8')).hexdigest()