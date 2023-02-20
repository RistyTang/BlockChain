from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
# OP_2DUP:用于将x和y压栈赋值
# OP_ADD:计算x+y
# OP_QUALVERIFY: 计算相加结果是否为2013
# OP_SUB: 计算x-y
# OP_EQUAL：验证是否为空，true则为非空
ex3a_txout_scriptPubKey = [OP_2DUP,OP_ADD,2013,OP_EQUALVERIFY,OP_SUB,535,OP_EQUAL]
######################################################################


#学号为2013536，为保证奇偶性，修改为2013535
if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0007 #设置分发金额为0.0007
    txid_to_spend = (
        '1641fe39ff2bd4873c27eb6710f4d6bd426ab249e6e473660533cf73a300f318')
    utxo_index = 0 #使用新币的第一份输出
    ######################################################################

    response = send_from_P2PKH_transaction(#调用ex1中的函数
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
