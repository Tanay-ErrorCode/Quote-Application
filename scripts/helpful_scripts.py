from brownie import accounts, network, config
import eth_utils

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['hardhat', 'development', 'ganache']

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    if network.show_active() in config["networks"]:
        return accounts.add(config['wallets']['from_key'])
    return None

