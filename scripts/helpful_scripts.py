from brownie import MockV3Aggregator, accounts, config, network
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork', 'main-fork-dev']
LOCAL_BLOCKCHAIN_ENVIRONMENTS  = ['development', 'ganache-local']
DECIMALS = 8
STARTING_PRICE = 2000*10**DECIMALS # Web3.toWei(STARTING_PRICE, 'ether')

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS) or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
    
def deploy_mocks():
    print(f'The activate network is {network.show_active()}')
    print('Deploing Mocks...')
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {'from':get_account()})
    print('Mocks deployed')
    