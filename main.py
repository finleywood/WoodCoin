import block

prevhash = input('Previous Hash: ')
numoft = int(input('Number of transactions: '))

i = 0
transactions = []
while i < numoft:
	trans = str(input('Transaction Details: '))
	transactions.append(trans)
	i = i + 1

print(transactions)

newblock = block.Block(prevhash=prevhash, transactions=transactions)

print(newblock)