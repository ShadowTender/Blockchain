import os
import time
from block_reader import *
from blockchain import Blockchain

path = '/root/D&K2/new data on web/lab5/lab_blockchain'

def nb_transactions():
	files = os.listdir(path+'/blocks')
	for name in files:
		with open(path+'/blocks/'+name, 'r') as  content:
			block  = read_block_json(content.read())
			print('Number of transactions of '+name+': {}'.format(len(block.transactions)))

def blocks_to_prove():
    files = os.listdir(path+'/blocks_to_prove')
    for name in files:
        with open(path+'/blocks_to_prove/'+name, "r") as content:
	        print(name+':')
	        block = read_block_json(content.read())
	        block.make_proof_ready()

def change_nb_zeors(filename,nb):
	with open(path+'/blocks_to_prove/'+filename, 'r') as file:
		block = read_block_json(file.read())
		block.set_zeros(nb)
		block.make_proof_ready()

def compute_wallet():
	files = os.listdir(path+'/blockchain_wallets')
	for name in files:
		with open(path+'/blockchain_wallets/'+name, "r") as content:
			print('Wallets of {}:'.format(name))
			chains = read_chain(content.read())
			chain = Blockchain()
			for block in chains:
				chain.add_block(block)
			print('{}\n'.format(chain.wallets))

def incorrect_block():
	files = os.listdir(path+'/blockchain_incorrect/')
	for name in files:
		with open(path+'/blockchain_incorrect/'+name,'r') as content:
			chains = read_chain(content.read())
			chain = Blockchain()
			valid=True
			for block in chains:
				if block.is_proof_ready():
					if check_transactions(chain, block, name):
						chain.add_block(block)
					else:
						valid=False
						break
				else:
					print('{} is incorrect: block index is {}, this block has not been proved!'.format(name,block.header.index))
					valid=False
					break
			if valid:
				print('{} is correct!'.format(name))

def check_transactions(chain, block, name):
        wallets = chain.wallets
        for trans in block.transactions:
            if trans.sender not in wallets:
                print('{} is incorrect: block index is {}, transaction index is {}'.format(name, block.header.index, trans.index))
                return False
            if trans.receiver not in wallets:
                wallets[trans.receiver]=0
            wallets[trans.sender]-=trans.amount
            wallets[trans.receiver]+=trans.amount
            for key in wallets:
                if wallets[key]<0:
                    print('{} is incorrect: block index is {}, transaction index is {}'.format(name, block.header.index, trans.index))
                    return False
        return True

if __name__ == '__main__':
	#Please uncomment the code when you need to get the result of related question

	#Ex 11.
	# nb_transactions()

	#Ex18.
	# blocks_to_prove()

	#Ex19.
	# filename = 'block4.json'
	# print('Change number of starting zeros for block4:\n')
	# for i in range(4,7,1):
	# 	start_time = time.time()
	# 	change_nb_zeors(filename ,i)
	# 	print('number of starting zeros:'+str(i)+', '+'execute_time: '+str(time.time()-start_time)+'s\n')

	#Ex.23(Delect transaction condition in add_block function) and Ex.24
	# compute_wallet()

	# Ex.25
	# incorrect_block()
	pass

	



