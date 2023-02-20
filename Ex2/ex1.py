from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address)


def P2PKH_scriptPubKey(address):#锁定脚本
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    # 复制栈顶元素（即压入公钥）
    # 将栈顶元素取出哈希后重新压入
    # 将公钥哈希值压入栈
    # 弹出栈顶的两个元素，比较它们是否相等
    # 用公钥检查一下签名是否正确
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):#解锁脚本
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction. You may need to use variables
    # that are globally defined.
    return [signature, my_public_key]
    ######################################################################


def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(my_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0005#要赎回的金额
    txid_to_spend = (
        'a93e884b671e0bcaf6ec605905616db063d2a37140bb6eff0dcfc86b17d90cf8')#之前分发时的哈希
    utxo_index = 0#使用第一份分发
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)#
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)