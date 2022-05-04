from brownie import myToken, web3
from scripts.helpful_scripts import get_account
from web3 import Web3 

initial_supply = Web3.toWei(1998, "ether")

def main():
    account = get_account()
    my_token = myToken.deploy(initial_supply, {"from": account})
    print(my_token.name())
    

