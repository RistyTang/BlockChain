from inspect import signature
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


#解决CBitcoinSecret报错
from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress

cust1_private_key = CBitcoinSecret(
    'cQcwJtZp9sAvtwdBwCbjc57wbsHvJkLkLjq7g7xH8r25VBUHUiAX')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cNwGZD8gBxZvyGYpow8LPmBbn5c91kNVksAcePQhNJwihY3tSRPb')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cRKnrsyVqK4xjUJVGRUhPBfRs7txVrt5SLJM4yuUk8YrRfXV7XLN')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

#首先是银行的公钥，这个是必须要有的
# 1是客户中需要认证的人数，3是总客户数，即只要3人中1个人的签名
# 之后是三个客户的公钥
ex2a_txout_scriptPubKey = [my_public_key,OP_CHECKSIGVERIFY,OP_1,cust1_public_key,cust2_public_key,cust3_public_key,OP_3,OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.001#我要加锁的金额为0.001
    txid_to_spend = (
        '26a4bd91a2fb030865fc0b9b6747aa99323ae6ad608ae4683f0ef418cbbaf75a')#之前分发时的哈希
    utxo_index = 0#用第8份分发验证cus1+cus2
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
