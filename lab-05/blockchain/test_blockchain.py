from blockchain import Blockchain
my_blokchain = Blockchain()

my_blokchain.add_transaction('Alice', 'Bob', 10)
my_blokchain.add_transaction('Bob', 'Charlie', 5)
my_blokchain.add_transaction('Charlie', 'Alice', 3)

previous_block = my_blokchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blokchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blokchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blokchain.create_block(new_proof, previous_hash)

for block in my_blokchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp: ",block.timestamp)
    print("Transaction: ",block.transactions)
    print("Proof: ",block.proof)
    print("Previous Hash: ", block.previous_hash)
    print("Hash: ",block.hash)
    print("------------------------------------")
    
print("Is Blockchain Valid: ",my_blokchain.is_chain_valid(my_blokchain.chain))