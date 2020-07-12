import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    difficulty = 5
    maxNonce =  4294967296 #2**32
    target = 2 ** (256-difficulty)

    block = Block("Genesis")
    pass_ = head = block

    def add(self, block):

        block.previous_hash = self.block.hash() #block at the top of the linked list
        block.blockNo = self.block.blockNo + 1  #next block

        self.block.next = block #pointer to the next block to add at the end of list
        self.block = self.block.next #move pointer up

    def mine(self, block):
        for n in range(self.maxNonce):
            guess = int(block.hash(), 16)
            if guess <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(50):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
    