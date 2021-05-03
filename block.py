import hashlib
import time
import datetime

class Block:
	def __init__(self, prevhash, transactions, timestamp=None):
		self.prevhash = prevhash
		self.transactions = transactions
		self.timestamp = timestamp or time.time()
		transstr = str(' '.join(self.transactions))
		self.data = prevhash + transstr + str(self.timestamp)

	def hash(self):
		return hashlib.sha256(self.data.encode()).hexdigest()

	def __repr__(self):
		return str({
			"prevHash": self.prevhash,
			"transactions": self.transactions,
			"timestamp": self.timestamp,
			"blockHash": self.hash()
		})