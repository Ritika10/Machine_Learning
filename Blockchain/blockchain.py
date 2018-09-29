## Reference : https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1,proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof : <<int> The proof given by the Proof of Work Algorithm:
        :param previous_hash : (Optional <str> Hash of previous block:
        :return: <dict> New Block:
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender:
        :param recipient:
        :param amount:
        :return:
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amoount' : amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block

        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the dictionary is ordered or we will have inconsisten hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

