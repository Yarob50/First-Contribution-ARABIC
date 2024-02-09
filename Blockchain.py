import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.proof = proof

def calculate_hash(index, previous_hash, timestamp, data, proof):
    value = f"{index}{previous_hash}{timestamp}{data}{proof}".encode()
    return hashlib.sha256(value).hexdigest()

def create_genesis_block():
    # Create the first block of the blockchain (genesis block)
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block", 0), 0)

def create_new_block(previous_block, data, proof):
    # Create a new block
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data, proof)
    return Block(index, previous_block.hash, timestamp, data, hash, proof)

def proof_of_work(previous_proof):
    # Simple proof of work algorithm to find a number that, when combined with the previous, gives a hash starting with "00"
    proof = 0
    while not valid_proof(previous_proof, proof):
        proof += 1
    return proof

def valid_proof(previous_proof, proof):
    # Validate the proof by checking if the hash starts with "00"
    guess = f"{previous_proof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:2] == "00"

# Create the blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks to add to the blockchain
num_blocks_to_add = 5

# Add blocks to the blockchain
for i in range(num_blocks_to_add):
    data = f"Block #{i + 1}"
    proof = proof_of_work(previous_block.proof)
    block = create_new_block(previous_block, data, proof)
    blockchain.append(block)
    previous_block = block

    print(f"Block #{block.index} has been added to the blockchain!")
    print(f"Hash: {block.hash}\n")

