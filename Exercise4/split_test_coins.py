from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress


from utils import create_txin, create_txout, broadcast_transaction


def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = my_address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = my_address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([my_private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              my_public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO: set these parameters correctly
    # Alice's private key:cNUEa7r7jHJ7wqA2BZSWDbPM5qDDZHsBpAVjbJJbg9E3S5rd9d8h   BTC
    # my_private_key = CBitcoinSecret('cNUEa7r7jHJ7wqA2BZSWDbPM5qDDZHsBpAVjbJJbg9E3S5rd9d8h')
    # Bob's private key:f4a0081d6a0464a0e1eeb6588489ebc74e868368a7e9e0df2bc99a7c62e999a1 BYC
    my_private_key = CBitcoinSecret.from_secret_bytes(x('f4a0081d6a0464a0e1eeb6588489ebc74e868368a7e9e0df2bc99a7c62e999a1'))

    my_public_key = my_private_key.pub
    my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

    amount_to_send = 0.009 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '3d1f0cac7a8b1ffe685c04793b36d3322e465456ce5e042bffd9a922b5a77449')
    utxo_index = 0
    n = 10 # number of outputs to split the input into
    network = 'bcy-test' # either 'btc-test3' or 'bcy-test'

    #
    #
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network)
