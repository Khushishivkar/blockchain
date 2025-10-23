# blockchain.py
import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_donations = []

        # Create genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'donations': self.current_donations,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset current donations
        self.current_donations = []
        self.chain.append(block)
        return block

    def new_donation(self, donor_id, donor_name, amount, organization):
        self.current_donations.append({
            'donor_id': donor_id,
            'donor_name': donor_name,
            'amount': amount,
            'organization': organization
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
