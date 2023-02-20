from bitcoin.core.script import *

######################################################################
# This function will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret 
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
# 
# TODO: Fill this in to create a script that is redeemable by both
#       of the above conditions.
# 
# See this page for opcode: https://en.bitcoin.it/wiki/Script
#
#

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        # fill this in!
        public_key_recipient,       #首先验证对方签名，两种方式都需要
        OP_CHECKSIGVERIFY, 
        OP_IF,                      #为1时，表明使用两个签名赎回
        public_key_sender,          #验证创建者签名
        OP_CHECKSIG, 
        OP_ELSE,                    #为0时表明用secret x赎回
        OP_HASH160,                 #进行哈希计算
        hash_of_secret,             #与所存的H（x）相比较
        OP_EQUAL, 
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        # fill this in!
        secret,
        OP_0, 
        sig_recipient
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        # fill this in!
        sig_sender,
        OP_1,
        sig_recipient
    ]

#
#
######################################################################

