from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import x

SelectParams('testnet')

######################################################################
# 
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cNUEa7r7jHJ7wqA2BZSWDbPM5qDDZHsBpAVjbJJbg9E3S5rd9d8h')

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cUGJ3Lt65TVHRD59BjroKj6vZcCGxZV9tbF7J5ECb2HHMwdaJqrQ')

######################################################################
#
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# token:c8a0cbdbe66d4be6974728f9ffcc2a10
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=c8a0cbdbe66d4be6974728f9ffcc2a10
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
#
# Send coins with 
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# 为bob领取测试币：
# curl -d '{"address": "C4CRBV1SjhXmy4DMazNpQDcgYpJiA6yBWG", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=c8a0cbdbe66d4be6974728f9ffcc2a10
# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('2e8da577813ffcfd5e7c5dd54dbc5150347167560e45ce32c4d279d99bdd9494'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('f4a0081d6a0464a0e1eeb6588489ebc74e868368a7e9e0df2bc99a7c62e999a1'))

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)

alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
