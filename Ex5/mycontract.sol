// Please paste your contract's solidity code here
// Note that writing a contract here WILL NOT deploy it and allow you to access it from your client
// You should write and develop your contract in Remix and then, before submitting, copy and paste it here

// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Splitwise
 * @dev maintain a debtbook and ensure that no cycles exist
 * @custom:dev-run-script ./scripts/deploy_with_web3.ts
 */
contract Splitwise {
    //debtbook['debtor']['creditor']保存debtor欠creditor的金额
    mapping(address => mapping(address => uint32)) debtbook;

    function lookup(address debtor, address creditor) external view returns (uint32 ret){
        return debtbook[debtor][creditor];
    }
    //先插入新边再消除环
    //插入边和删除环必须在一个函数内进行，否则会破坏原子性造成错误
    /** 
     * @param path 欲消去的环，方向由debtor指向creditor，起点与终点必须一致
     * @param flow 环上欲消去的金额，0代表无环
     */
    function add_IOU_chain(address creditor, uint32 amount, address[] calldata path, uint32 flow) external{
        //为防止恶意抹去交易，必须保证数量为正
        require(amount > 0, "transaction amount must be positive!");
        //为防止前端恶意发起溢出攻击，必须防止自环
        require(creditor != msg.sender, "debtor and creditor cannot be the same!");
        //起点与终点必须一致
        require(path[0] == path[path.length-1]);
        //STEP 1: 加入新交易
        debtbook[msg.sender][creditor] += amount;
        //此时图中存在环
        //STEP 2: 消除环
        if(flow > 0){
            //如果不是环，退出
            require(path[0]==path[path.length - 1], "path must be a loop!");
            for(uint i = 0;i < path.length - 1;i++){
                //如果环路不完整，退出
                require(debtbook[path[i]][path[i+1]] >= flow, "loop incomplete!");
                //更新环上的每条路径
                debtbook[path[i]][path[i+1]] -= flow;
            }
        }
    }
}