from brownie import Lottery, network, config
from scripts.helpful_scripts import get_account, get_contract


def deploy_lottery():
    account = get_account(id="freecodecamp-account")
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify", False),
    )


def start_lottery():
    account = get_account(id="freecodecamp-account")
    lottery = Lottery[-1]
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    print("The lottery is started!")


def main():
    deploy_lottery()
    start_lottery()
