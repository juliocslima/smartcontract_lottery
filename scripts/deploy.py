from brownie import Lottery, network, config, accounts
from web3 import Web3


def deploy_lottery():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    print(lottery.getLatestPrice())


def main():
    deploy_lottery()
