import datetime as date
import Block


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_data = "Hey! I'm block " + str(this_index)
    return Block(this_index, date.datetime.now(), this_data, last_block.hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks = 20

for i in range(0, num_of_blocks):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the blockchain".format(block_to_add.index))
    print("Hash: {}n".format(block_to_add.hash))
